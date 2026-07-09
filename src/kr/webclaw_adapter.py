"""WebClaw → Online-Mind2Web v2 trajectory adapter.

WebClaw (https://github.com/DureClaw/webclaw) is a Chrome MV3 extension that
joins a DureClaw fleet as a browser node.  The master brain sends instructions
such as ``[CLICK] selector``, ``[CLICKTEXT] label``, ``[DOM] css``, ``[FILL]
selector = value`` over a Phoenix-Channel WebSocket bus; webclaw executes them
in a real browser tab and returns the result text.

This module converts a log of webclaw task frames into the Online-Mind2Web v2
submission schema (``data/schema_v2/README.md``) so the existing WebJudge
evaluator (``src/run.py``) can score KR-benchmark trajectories produced by a
webclaw-driven agent.

WebClaw action grammar → v2 ActionStep mapping
==============================================

| WebClaw marker      | v2 verb       | notes                                         |
|---------------------|---------------|-----------------------------------------------|
| [OPEN] <url>        | NAVIGATE      | url field set from the argument                |
| [CLICK] <sel>       | CLICK         | target = selector or coords(x,y)              |
| [CLICKTEXT] <label> | CLICK         | target = coords/text(label); Grammar B style  |
| [FILL]/[TYPE] s=v   | TYPE          | text content = value                           |
| [SUBMIT] <sel>      | PRESS_KEY     | Enter submit (closest v2 verb)                |
| [JS] <code>         | (WAIT)        | observation step; not a user-visible action   |
| [DOM] <css>         | (WAIT)        | observation step                              |
| [SNAP]              | (WAIT)        | baseline snapshot                             |
| [DIFF] <action>     | (action)      | unwrap the inner action                       |
| [SCROLL] (future)   | SCROLL        |                                               |
| final answer        | TASK_COMPLETE | from agent_final_answer                       |

Screenshot handling
===================
WebClaw's ``[SCREENSHOT]`` is on the roadmap and not yet in core.js.  Until it
ships, this adapter accepts screenshots from an external capturer (e.g. the
Chrome ``captureVisibleTab`` API exposed via a small content-script bridge, or
a puppeteer watcher).  Provide them as a list of file names aligned 1:1 with
the action log; missing screenshots are filled with a placeholder and a
warning is emitted.
"""
from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class WebclawFrame:
    """A single webclaw task frame (instruction + result)."""

    instruction: str
    result: str = ""
    status: str = "done"        # "done" | "failed"
    url: str | None = None      # page url at the time of the action, if known
    screenshot: str | None = None  # filename in trajectory/, if captured
    thought: str | None = None  # optional reasoning supplied by the master brain
    timestamp_ms: int | None = None


@dataclass
class V2Trajectory:
    """In-memory builder for a v2 result.json document."""

    task: str
    task_id: str
    reference_length: int
    agent_final_answer: str = ""
    steps: list[dict[str, Any]] = field(default_factory=list)

    def add_step(
        self,
        action: str,
        thought: str | None,
        screenshot: str,
        url: str | None = None,
        action_status: str | None = None,
    ) -> None:
        step_idx = len(self.steps)
        self.steps.append(
            {
                "step": step_idx,
                "screenshot": screenshot,
                "url": url or "",
                "action": action,
                "action_status": action_status,
                "thought": thought,
            }
        )

    def finalize(self) -> dict[str, Any]:
        return {
            "schema_version": "online-mind2web-v2",
            "task": self.task,
            "task_id": self.task_id,
            "agent_final_answer": self.agent_final_answer,
            "reference_length": self.reference_length,
            "action_history": list(self.steps),
        }


# ---------------------------------------------------------------------------
# Marker parsing (mirrors core.js parseMarker / splitSelVal)
# ---------------------------------------------------------------------------

_MARKER_RE = re.compile(
    r"^\[([A-Z]+\??)(?:@([^\]]+))?\]\s*(.*)$", re.DOTALL
)


def parse_marker(text: str) -> tuple[str | None, str, str | None]:
    """Return (marker_name, rest, url_match) or (None, text, None)."""
    m = _MARKER_RE.match(text.strip())
    if not m:
        return None, text.strip(), None
    return m.group(1).upper(), m.group(3), (m.group(2) or "").strip() or None


def split_sel_val(rest: str) -> tuple[str, str]:
    """Split ``selector = value`` or ``selector\\nvalue``."""
    nl = rest.find("\n")
    if nl >= 0:
        return rest[:nl].strip(), rest[nl + 1:]
    eq = rest.find(" = ")
    if eq >= 0:
        return rest[:eq].strip(), rest[eq + 3:]
    return rest.strip(), ""


# ---------------------------------------------------------------------------
# Frame → v2 action string conversion
# ---------------------------------------------------------------------------

def _status_suffix(status: str | None) -> str:
    if status == "failed":
        return " | FAILED"
    if status == "done":
        return " | SUCCESS"
    return ""


def frame_to_action(frame: WebclawFrame) -> tuple[str, str | None, str | None]:
    """Convert a single WebclawFrame to (action_string, verb, action_status).

    ``verb`` is the Grammar-A verb (NAVIGATE, CLICK, TYPE, …) or ``None`` for
    observation-only steps that map to WAIT.
    """
    instr = frame.instruction.strip()
    marker, rest, url_match = parse_marker(instr)
    status = frame.status if frame.status != "done" else None  # only mark failures explicitly
    suffix = _status_suffix(frame.status)

    if marker is None:
        # No marker → LLM delegation / free text.  Treat as WAIT (observation).
        return f"WAIT page -> {instr[:120]}{suffix}", "WAIT", frame.status or "SUCCESS"

    if marker == "OPEN":
        return f"page -> NAVIGATE -> {rest.strip()}{suffix}", "NAVIGATE", frame.status or "SUCCESS"

    if marker == "CLICK":
        return f"CLICK {rest.strip()} -> {rest.strip()}{suffix}", "CLICK", frame.status or "SUCCESS"

    if marker == "CLICKTEXT":
        return f"CLICK text({rest.strip()}) -> click visible text '{rest.strip()}'{suffix}", "CLICK", frame.status or "SUCCESS"

    if marker in ("FILL", "TYPE"):
        sel, val = split_sel_val(rest)
        return f"TYPE {sel} -> type '{val[:80]}'{suffix}", "TYPE", frame.status or "SUCCESS"

    if marker == "SUBMIT":
        return f"PRESS_KEY page -> submit form via {rest.strip()}{suffix}", "PRESS_KEY", frame.status or "SUCCESS"

    if marker == "DOM":
        return f"WAIT page -> observe DOM: {rest.strip()[:80]}{suffix}", "WAIT", frame.status or "SUCCESS"

    if marker == "LINKS":
        return f"WAIT page -> extract links: {rest.strip()[:80]}{suffix}", "WAIT", frame.status or "SUCCESS"

    if marker == "ATTR":
        return f"WAIT page -> read attributes: {rest.strip()[:80]}{suffix}", "WAIT", frame.status or "SUCCESS"

    if marker == "JS":
        return f"WAIT page -> execute JS: {rest.strip()[:60]}…{suffix}", "WAIT", frame.status or "SUCCESS"

    if marker == "SNAP":
        return f"WAIT page -> DOM baseline snapshot{suffix}", "WAIT", frame.status or "SUCCESS"

    if marker == "DIFF":
        # Unwrap the inner action and convert recursively.
        inner_frame = WebclawFrame(
            instruction=rest,
            result=frame.result,
            status=frame.status,
            url=frame.url,
            screenshot=frame.screenshot,
            thought=frame.thought,
        )
        inner_action, inner_verb, inner_status = frame_to_action(inner_frame)
        return (
            f"{inner_action} (via DIFF){suffix}",
            inner_verb,
            inner_status,
        )

    if marker == "TABS":
        return f"WAIT page -> list open tabs{suffix}", "WAIT", frame.status or "SUCCESS"

    if marker == "FETCH":
        return f"WAIT page -> fetch URL: {rest.strip()[:80]}{suffix}", "WAIT", frame.status or "SUCCESS"

    if marker == "HUD":
        return f"WAIT page -> toggle HUD: {rest.strip()}{suffix}", "WAIT", frame.status or "SUCCESS"

    if marker == "SAY":
        return f"WAIT page -> master says: {rest.strip()[:80]}{suffix}", "WAIT", frame.status or "SUCCESS"

    # Unknown marker → observation
    return f"WAIT page -> {marker}: {rest.strip()[:80]}{suffix}", "WAIT", frame.status or "SUCCESS"


# ---------------------------------------------------------------------------
# Screenshot helpers
# ---------------------------------------------------------------------------

def _screenshot_name(index: int) -> str:
    return f"{index:04d}.png"


def _resolve_screenshot(
    frame: WebclawFrame,
    index: int,
    screenshots: list[str] | None,
) -> str:
    """Determine the screenshot filename for step *index*."""
    if frame.screenshot:
        return frame.screenshot
    if screenshots and index < len(screenshots):
        return screenshots[index]
    # Placeholder — the validator will warn but not fail.
    return _screenshot_name(index)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def frames_to_v2(
    task: str,
    task_id: str,
    reference_length: int,
    frames: list[WebclawFrame],
    agent_final_answer: str,
    screenshots: list[str] | None = None,
) -> dict[str, Any]:
    """Convert a list of :class:`WebclawFrame` into a v2 result.json dict.

    Parameters
    ----------
    task
        Task description (Korean or English).
    task_id
        Bare task id hash (no ``tasks/`` prefix).
    reference_length
        Human reference length from the task definition.
    frames
        Ordered list of webclaw task frames.
    agent_final_answer
        The agent's final answer text.
    screenshots
        Optional list of screenshot filenames aligned 1:1 with *frames*.
        If ``None`` or too short, placeholder names are generated.
    """
    traj = V2Trajectory(
        task=task,
        task_id=task_id,
        reference_length=reference_length,
        agent_final_answer=agent_final_answer,
    )

    for i, frame in enumerate(frames):
        action, _verb, action_status = frame_to_action(frame)
        screenshot = _resolve_screenshot(frame, i, screenshots)
        thought = frame.thought
        # Normalise webclaw status ("done"/"failed") to v2 ("SUCCESS"/"FAILED").
        v2_status = "FAILED" if action_status == "failed" else "SUCCESS"
        traj.add_step(
            action=action,
            thought=thought,
            screenshot=screenshot,
            url=frame.url,
            action_status=v2_status,
        )

    # Terminal step
    terminal_step = len(traj.steps)
    traj.add_step(
        action=f"TASK_COMPLETE -> ANSWER: {agent_final_answer}",
        thought="Task completed.",
        screenshot=_screenshot_name(terminal_step),
        url=frames[-1].url if frames else "",
        action_status=None,
    )

    return traj.finalize()


def write_trajectory(
    output_dir: str,
    task: str,
    task_id: str,
    reference_length: int,
    frames: list[WebclawFrame],
    agent_final_answer: str,
    screenshots: list[str] | None = None,
) -> str:
    """Write a complete v2 submission to ``<output_dir>/<task_id>/``.

    Creates ``result.json`` and (optionally) copies screenshot files into
    ``trajectory/``.  Returns the path to the written ``result.json``.
    """
    task_dir = os.path.join(output_dir, task_id)
    traj_dir = os.path.join(task_dir, "trajectory")
    os.makedirs(traj_dir, exist_ok=True)

    doc = frames_to_v2(
        task=task,
        task_id=task_id,
        reference_length=reference_length,
        frames=frames,
        agent_final_answer=agent_final_answer,
        screenshots=screenshots,
    )

    result_path = os.path.join(task_dir, "result.json")
    with open(result_path, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)

    return result_path


# ---------------------------------------------------------------------------
# CLI: convert a webclaw session log JSON into v2 trajectory files
# ---------------------------------------------------------------------------

def _load_frames_log(path: str) -> list[WebclawFrame]:
    """Load a webclaw session log (JSON array or JSONL)."""
    frames: list[WebclawFrame] = []
    with open(path, encoding="utf-8") as f:
        content = f.read().strip()
    if content[0] == "[":
        items = json.loads(content)
    else:
        items = [json.loads(line) for line in content.splitlines() if line.strip()]
    for item in items:
        frames.append(
            WebclawFrame(
                instruction=item.get("instruction") or item.get("instructions") or "",
                result=item.get("result") or item.get("output") or "",
                status=item.get("status", "done"),
                url=item.get("url"),
                screenshot=item.get("screenshot"),
                thought=item.get("thought"),
                timestamp_ms=item.get("timestamp_ms"),
            )
        )
    return frames


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert a webclaw session log into Online-Mind2Web v2 trajectory files.",
    )
    parser.add_argument("--log", required=True, help="Path to webclaw session log (JSON or JSONL)")
    parser.add_argument("--task-id", required=True, help="Task id (bare hash)")
    parser.add_argument("--task", required=True, help="Task description")
    parser.add_argument("--reference-length", type=int, default=8)
    parser.add_argument("--final-answer", required=True, help="Agent's final answer text")
    parser.add_argument("--screenshots-dir", default=None, help="Directory of screenshot PNGs (sorted)")
    parser.add_argument("--output-dir", default="./data/kr/trajectories", help="Output directory")
    args = parser.parse_args()

    frames = _load_frames_log(args.log)

    screenshots = None
    if args.screenshots_dir and os.path.isdir(args.screenshots_dir):
        from pathlib import Path
        screenshots = sorted(
            p.name for p in Path(args.screenshots_dir).iterdir()
            if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")
        )

    path = write_trajectory(
        output_dir=args.output_dir,
        task=args.task,
        task_id=args.task_id,
        reference_length=args.reference_length,
        frames=frames,
        agent_final_answer=args.final_answer,
        screenshots=screenshots,
    )
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()