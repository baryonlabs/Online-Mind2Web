"""Run KR-benchmark tasks through a WebClaw fleet node and collect v2 trajectories.

This orchestrator is the *master brain* side: for each KR task it

1. loads the task definition from ``data/kr/tasks/<task_id>.json``
2. sends the ``website`` URL as an ``[OPEN]`` instruction to webclaw
3. delegates the task description to the master LLM (or a configured brain URL)
   which issues further ``[CLICK]`` / ``[FILL]`` / ``[DOM]`` … markers
4. collects every ``task.assign → task.result`` frame into a session log
5. converts the session log into a v2 ``result.json`` via
   :mod:`src.kr.webclaw_adapter`

Because webclaw speaks a plain Phoenix-Channel WebSocket, this runner can talk
to a live browser node without any extra SDK.

Usage::

    python3 script/run_webclaw_kr.py \\
        --bus ws://localhost:4000 \\
        --token <secret> \\
        --work-key <key> \\
        --node-name webclaw@chrome-1 \\
        --brain-url http://localhost:8000 \\
        --brain-token <token> \\
        --output-dir ./data/kr/trajectories \\
        --task-ids all

You can limit to specific tasks with ``--task-ids <id1>,<id2>`` or
``--domain "Housing & Real Estate"``.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
import time
from pathlib import Path

# Make src importable when run from repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from kr.webclaw_adapter import (  # noqa: E402
    WebclawFrame,
    write_trajectory,
)

KR_TASKS_DIR = Path(__file__).resolve().parent.parent / "data" / "kr" / "tasks"


# ---------------------------------------------------------------------------
# Task loading
# ---------------------------------------------------------------------------

def load_kr_tasks(
    task_ids: list[str] | None = None,
    domain: str | None = None,
) -> list[dict]:
    tasks = []
    for fn in sorted(KR_TASKS_DIR.iterdir()):
        if not fn.suffix == ".json":
            continue
        with fn.open(encoding="utf-8") as f:
            t = json.load(f)
        if task_ids and "all" not in task_ids and t["task_id"] not in task_ids:
            continue
        if domain and t.get("domain") != domain:
            continue
        tasks.append(t)
    return tasks


# ---------------------------------------------------------------------------
# Minimal Phoenix-Channel WebSocket client (matches webclaw core.js)
# ---------------------------------------------------------------------------

class WebclawMaster:
    """Thin async WebSocket client that dispatches tasks to a webclaw node."""

    def __init__(
        self,
        bus: str,
        token: str,
        work_key: str,
        node_name: str,
        brain_url: str | None = None,
        brain_token: str | None = None,
    ):
        self.bus = bus
        self.token = token
        self.work_key = work_key
        self.node_name = node_name
        self.brain_url = brain_url
        self.brain_token = brain_token
        self._ws: "asyncio.websockets" = None  # noqa: F821
        self._ref = 0
        self._join_ref = None
        self._pending: dict[str, asyncio.Future] = {}

    def _nref(self) -> str:
        self._ref += 1
        return str(self._ref)

    def _url(self) -> str:
        host = self.bus.replace("ws://", "").replace("wss://", "")
        scheme = "wss" if self.bus.startswith("wss://") else "ws"
        return f"{scheme}://{host}/socket/websocket?vsn=2.0.0&token={self.token}"

    async def connect(self) -> None:
        try:
            import websockets
        except ImportError:
            print(
                "ERROR: 'websockets' package is required.  Install with:\n"
                "  pip install websockets",
                file=sys.stderr,
            )
            sys.exit(1)
        self._ws = await websockets.connect(self._url())
        self._join_ref = self._nref()
        await self._ws.send(json.dumps([
            self._join_ref, self._join_ref,
            f"work:{self.work_key}", "phx_join",
            {
                "agent_name": "master@runner",
                "role": "controller",
                "machine": "python",
                "capabilities": ["controller", "llm"],
                "preferred_model": "gpt-4o",
                "version": "kr-runner/0.1",
            },
        ]))
        print(f"[master] joined work:{self.work_key}", file=sys.stderr)

    async def _recv_loop(self) -> None:
        async for raw in self._ws:
            try:
                frame = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if not isinstance(frame, list) or len(frame) != 5:
                continue
            event = frame[3]
            payload = frame[4]
            if event == "task.result" and payload.get("task_id") in self._pending:
                fut = self._pending.pop(payload["task_id"])
                fut.set_result(payload)
            elif event == "task.ack":
                # Delivery ack — just log it.
                print(f"[master] ack {payload.get('task_id')}", file=sys.stderr)

    async def send_task(
        self,
        instruction: str,
        task_id: str,
        timeout: float = 120.0,
    ) -> dict:
        """Send a single instruction to the webclaw node and await the result."""
        fut: asyncio.Future = asyncio.get_event_loop().create_future()
        self._pending[task_id] = fut
        await self._ws.send(json.dumps([
            self._join_ref, self._nref(),
            f"work:{self.work_key}", "task.assign",
            {
                "task_id": task_id,
                "to": self.node_name,
                "from": "master@runner",
                "instructions": instruction,
            },
        ]))
        try:
            return await asyncio.wait_for(fut, timeout=timeout)
        except asyncio.TimeoutError:
            self._pending.pop(task_id, None)
            return {"task_id": task_id, "status": "failed", "output": "[timeout]"}

    async def close(self) -> None:
        if self._ws:
            await self._ws.close()


# ---------------------------------------------------------------------------
# Per-task execution
# ---------------------------------------------------------------------------

async def run_task(
    master: WebclawMaster,
    task: dict,
    output_dir: str,
    max_steps: int = 30,
    step_timeout: float = 60.0,
) -> str:
    """Run a single KR task through webclaw and write a v2 trajectory."""
    task_id = task["task_id"]
    website = task["website"]
    desc = task["task_description"]
    ref_len = task["reference_length"]

    print(f"\n{'='*60}")
    print(f"Task {task_id}: {desc[:70]}...")
    print(f"Start URL: {website}")
    print(f"{'='*60}")

    frames: list[WebclawFrame] = []

    # Step 0: navigate to the starting URL.
    nav_result = await master.send_task(
        instruction=f"[OPEN] {website}",
        task_id=f"{task_id}-step0",
        timeout=step_timeout,
    )
    frames.append(WebclawFrame(
        instruction=f"[OPEN] {website}",
        result=nav_result.get("output", ""),
        status=nav_result.get("status", "done"),
        url=website,
        thought=f"태스크 시작: {website}로 이동",
    ))
    page_url = website

    # Steps 1..N: delegate to the master brain.
    # The brain is expected to issue webclaw markers ([CLICK], [DOM], etc.)
    # and return them as instructions.  Here we send the task description +
    # the last observation to the brain, and the brain responds with the next
    # webclaw instruction.
    last_output = nav_result.get("output", "")
    final_answer = ""

    for step in range(1, max_steps + 1):
        # Ask the brain for the next action.
        brain_instruction = await _ask_brain(
            master,
            desc,
            last_output,
            step,
            max_steps,
        )

        if brain_instruction is None:
            final_answer = "에이전트가 태스크를 완료하지 못했습니다."
            break

        if brain_instruction.upper().startswith("TASK_COMPLETE"):
            # Extract answer after "TASK_COMPLETE:" or "DONE:"
            answer_text = re.split(r"TASK_COMPLETE:?\s*", brain_instruction, maxsplit=1, flags=re.IGNORECASE)
            final_answer = answer_text[1].strip() if len(answer_text) > 1 else "태스크 완료."
            break

        # Send the brain's instruction to webclaw.
        result = await master.send_task(
            instruction=brain_instruction,
            task_id=f"{task_id}-step{step}",
            timeout=step_timeout,
        )
        last_output = result.get("output", "")
        page_url = result.get("url", page_url)

        frames.append(WebclawFrame(
            instruction=brain_instruction,
            result=last_output,
            status=result.get("status", "done"),
            url=page_url,
            thought=None,  # brain can supply thoughts separately
        ))

        if result.get("status") == "failed":
            print(f"  step {step} FAILED: {last_output[:80]}", file=sys.stderr)

    if not final_answer:
        final_answer = f"태스크 '{desc[:50]}' 수행을 시도했으나 완료 여부를 확인하지 못했습니다."

    # Write v2 trajectory.
    result_path = write_trajectory(
        output_dir=output_dir,
        task=desc,
        task_id=task_id,
        reference_length=ref_len,
        frames=frames,
        agent_final_answer=final_answer,
    )
    print(f"  → wrote {result_path}")
    return result_path


async def _ask_brain(
    master: WebclawMaster,
    task_desc: str,
    last_observation: str,
    step: int,
    max_steps: int,
) -> str | None:
    """Ask the master brain for the next webclaw instruction.

    If no brain URL is configured, return ``None`` (task aborts).
    In a real deployment the brain is an LLM endpoint that returns a single
    webclaw marker instruction (``[CLICK] …``, ``[DOM] …``, ``TASK_COMPLETE …``).
    """
    if not master.brain_url:
        print("  [warn] no brain URL configured — aborting after navigation", file=sys.stderr)
        return None

    import urllib.request
    prompt = (
        f"당신은 웹 브라우저를 조작하는 에이전트입니다. 다음 태스크를 수행하세요.\n\n"
        f"태스크: {task_desc}\n\n"
        f"직전 관찰 결과 (truncated):\n{last_observation[:2000]}\n\n"
        f"다음 동작을 WebClaw 마커 형식으로 한 줄로 출력하세요.\n"
        f"사용 가능 마커: [OPEN] [CLICK] [CLICKTEXT] [FILL] [SUBMIT] [DOM] [LINKS] [JS] [SNAP] [DIFF] [TABS]\n"
        f"태스크가 완료되었으면 'TASK_COMPLETE: <답변>' 출력하세요.\n"
        f"현재 스텝: {step}/{max_steps}"
    )
    body = json.dumps({"prompt": prompt}).encode()
    req = urllib.request.Request(
        master.brain_url.rstrip("/") + "/brain/exec",
        data=body,
        headers={
            "content-type": "application/json",
            **({"authorization": f"Bearer {master.brain_token}"} if master.brain_token else {}),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
            return data.get("output") or data.get("instruction") or None
    except Exception as e:
        print(f"  [brain error] {e}", file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def main_async(args: argparse.Namespace) -> None:
    tasks = load_kr_tasks(
        task_ids=args.task_ids.split(",") if args.task_ids else None,
        domain=args.domain,
    )
    if not tasks:
        print("No tasks matched the filter.", file=sys.stderr)
        return
    print(f"Loaded {len(tasks)} KR tasks", file=sys.stderr)

    master = WebclawMaster(
        bus=args.bus,
        token=args.token,
        work_key=args.work_key,
        node_name=args.node_name,
        brain_url=args.brain_url,
        brain_token=args.brain_token,
    )
    await master.connect()

    # Start the recv loop in the background.
    recv_task = asyncio.create_task(master._recv_loop())

    os.makedirs(args.output_dir, exist_ok=True)

    results = []
    for task in tasks:
        try:
            path = await run_task(
                master,
                task,
                output_dir=args.output_dir,
                max_steps=args.max_steps,
                step_timeout=args.step_timeout,
            )
            results.append(path)
        except Exception as e:
            print(f"  [error] {e}", file=sys.stderr)
            results.append(None)

    recv_task.cancel()
    await master.close()

    print(f"\nDone. {sum(1 for r in results if r)}/{len(tasks)} trajectories written to {args.output_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run KR-benchmark tasks through a WebClaw browser node.",
    )
    parser.add_argument("--bus", required=True, help="WebSocket bus URL (ws://host:port)")
    parser.add_argument("--token", required=True, help="Bus auth token")
    parser.add_argument("--work-key", required=True, help="Work key (Phoenix channel topic)")
    parser.add_argument("--node-name", default="webclaw@chrome-1", help="Target webclaw node name")
    parser.add_argument("--brain-url", default=None, help="Master brain LLM endpoint")
    parser.add_argument("--brain-token", default=None, help="Master brain auth token")
    parser.add_argument("--output-dir", default="./data/kr/trajectories")
    parser.add_argument("--task-ids", default="all", help="Comma-separated task ids or 'all'")
    parser.add_argument("--domain", default=None, help="Filter by domain")
    parser.add_argument("--max-steps", type=int, default=30)
    parser.add_argument("--step-timeout", type=float, default=60.0)
    args = parser.parse_args()

    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()