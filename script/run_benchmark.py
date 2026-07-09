#!/usr/bin/env python3
"""One-command KR benchmark runner: config → WebClaw execution → WebJudge evaluation → score.

Usage:
    # 1. Copy config template and fill in your values
    cp config.json.example config.local.json
    # Edit config.local.json with your bus/token/brain/openai key

    # 2. Run the full pipeline
    python3 script/run_benchmark.py

    # 3. Or run only a subset
    python3 script/run_benchmark.py --bundle legal          # one bundle
    python3 script/run_benchmark.py --domain "Education"     # one domain
    python3 script/run_benchmark.py --difficulty easy        # one difficulty
    python3 script/run_benchmark.py --task-ids abc,def       # specific tasks
    python3 script/run_benchmark.py --limit 10               # first 10 tasks
    python3 script/run_benchmark.py --skip-exec              # eval only (trajectories exist)
    python3 script/run_benchmark.py --skip-eval              # exec only (no WebJudge)
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KR_TASKS_DIR = ROOT / "data" / "kr" / "tasks"
CONFIG_PATH = ROOT / "config.local.json"

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║  Online-Mind2Web KR Benchmark — Full Pipeline Runner         ║
║  WebClaw execution → v2 trajectory → WebJudge evaluation      ║
╚══════════════════════════════════════════════════════════════╝
"""


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

def load_config(path: Path = CONFIG_PATH) -> dict:
    if not path.exists():
        print(f"ERROR: config file not found: {path}", file=sys.stderr)
        print("Run: cp config.json.example config.local.json", file=sys.stderr)
        print("Then edit config.local.json with your credentials.", file=sys.stderr)
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        # Strip JSON comments (lines starting with //)
        lines = []
        for line in f:
            stripped = line.strip()
            if stripped.startswith('"//'):
                continue
            lines.append(line)
        cfg = json.loads("".join(lines))
    # Validate required fields
    required = ["bus", "token", "work_key", "node_name", "openai_key"]
    missing = [k for k in required if cfg.get(k, "REPLACE_ME") == "REPLACE_ME"]
    if missing:
        print(f"ERROR: config.local.json has placeholder values for: {missing}", file=sys.stderr)
        print("Edit config.local.json and fill in real values.", file=sys.stderr)
        sys.exit(1)
    return cfg


# ---------------------------------------------------------------------------
# Task loading & filtering
# ---------------------------------------------------------------------------

def load_tasks(
    task_ids: str | None = None,
    bundle: str | None = None,
    domain: str | None = None,
    difficulty: str | None = None,
    limit: int | None = None,
) -> list[dict]:
    tasks = []
    for fn in sorted(KR_TASKS_DIR.iterdir()):
        if fn.suffix != ".json":
            continue
        with fn.open(encoding="utf-8") as f:
            t = json.load(f)
        if task_ids and "all" not in task_ids:
            ids = [x.strip() for x in task_ids.split(",")]
            if t["task_id"] not in ids:
                continue
        if bundle and t.get("baryon_bundle") != bundle:
            continue
        if domain and t.get("domain") != domain:
            continue
        if difficulty and t.get("difficulty") != difficulty:
            continue
        tasks.append(t)
    if limit:
        tasks = tasks[:limit]
    return tasks


# ---------------------------------------------------------------------------
# Phase 1: WebClaw execution → trajectories
# ---------------------------------------------------------------------------

def run_webclaw(cfg: dict, tasks: list[dict], output_dir: str) -> bool:
    """Run script/run_webclaw_kr.py with config values. Returns True on success."""
    print(f"\n{'='*60}")
    print(f"Phase 1: WebClaw execution ({len(tasks)} tasks)")
    print(f"  Bus:       {cfg['bus']}")
    print(f"  Node:      {cfg['node_name']}")
    print(f"  Brain:     {cfg.get('brain_url', '(none)')}")
    print(f"  Output:    {output_dir}")
    print(f"{'='*60}\n")

    task_id_list = ",".join(t["task_id"] for t in tasks)

    cmd = [
        sys.executable, str(ROOT / "script" / "run_webclaw_kr.py"),
        "--bus", cfg["bus"],
        "--token", cfg["token"],
        "--work-key", cfg["work_key"],
        "--node-name", cfg["node_name"],
        "--output-dir", output_dir,
        "--task-ids", task_id_list,
        "--max-steps", str(cfg.get("max_steps", 30)),
        "--step-timeout", str(cfg.get("step_timeout", 60)),
    ]
    if cfg.get("brain_url"):
        cmd += ["--brain-url", cfg["brain_url"]]
    if cfg.get("brain_token"):
        cmd += ["--brain-token", cfg["brain_token"]]

    print(f"Running: {' '.join(cmd[:6])} ...")
    result = subprocess.run(cmd, cwd=str(ROOT))
    if result.returncode != 0:
        print(f"\nERROR: WebClaw runner exited with code {result.returncode}", file=sys.stderr)
        return False

    # Count generated trajectories
    traj_dir = Path(output_dir)
    count = sum(1 for d in traj_dir.iterdir() if d.is_dir() and (d / "result.json").exists()) if traj_dir.exists() else 0
    print(f"\n✓ Generated {count} trajectories in {output_dir}")
    return True


# ---------------------------------------------------------------------------
# Phase 2: WebJudge evaluation
# ---------------------------------------------------------------------------

def run_eval(cfg: dict, trajectories_dir: str) -> str:
    """Run src/run.py with WebJudge. Returns the output path."""
    model = cfg.get("eval_model", "o4-mini")
    mode = "WebJudge_Online_Mind2Web_eval"
    output_path = f"{trajectories_dir}_result"

    print(f"\n{'='*60}")
    print(f"Phase 2: WebJudge evaluation")
    print(f"  Model:          {model}")
    print(f"  Mode:           {mode}")
    print(f"  Trajectories:   {trajectories_dir}")
    print(f"  Output:         {output_path}")
    print(f"{'='*60}\n")

    cmd = [
        sys.executable, str(ROOT / "src" / "run.py"),
        "--mode", mode,
        "--model", model,
        "--trajectories_dir", trajectories_dir,
        "--api_key", cfg["openai_key"],
        "--output_path", output_path,
        "--num_worker", str(cfg.get("num_workers", 1)),
        "--score_threshold", "3",
    ]

    print(f"Running: python3 src/run.py --mode {mode} --model {model} ...")
    result = subprocess.run(cmd, cwd=str(ROOT))
    if result.returncode != 0:
        print(f"\nERROR: WebJudge evaluation exited with code {result.returncode}", file=sys.stderr)
        return ""

    print(f"\n✓ Evaluation results written to {output_path}")
    return output_path


# ---------------------------------------------------------------------------
# Phase 3: Score summary
# ---------------------------------------------------------------------------

def compute_score(output_path: str, total_tasks: int) -> dict:
    """Parse the WebJudge results JSONL and compute success rate."""
    result_file = None
    result_dir = Path(output_path)
    if result_dir.is_dir():
        for fn in result_dir.iterdir():
            if fn.name.endswith("_auto_eval_results.json"):
                result_file = fn
                break

    if not result_file or not result_file.exists():
        print(f"WARNING: no results file found in {output_path}", file=sys.stderr)
        return {"total": total_tasks, "evaluated": 0, "success": 0, "rate": 0.0}

    evaluated = 0
    success = 0
    bundle_stats: dict[str, dict] = {}

    with open(result_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            label = item.get("predicted_label", 0)
            evaluated += 1
            if label == 1:
                success += 1

            # Track bundle-level stats
            bundle = item.get("baryon_bundle", "(original)")
            if bundle not in bundle_stats:
                bundle_stats[bundle] = {"total": 0, "success": 0}
            bundle_stats[bundle]["total"] += 1
            if label == 1:
                bundle_stats[bundle]["success"] += 1

    rate = (success / evaluated * 100) if evaluated > 0 else 0.0

    print(f"\n{'='*60}")
    print(f"Phase 3: Score Summary")
    print(f"{'='*60}")
    print(f"\n  Total tasks:     {total_tasks}")
    print(f"  Evaluated:       {evaluated}")
    print(f"  Success:         {success}")
    print(f"  Success rate:    {rate:.1f}%")

    if bundle_stats:
        print(f"\n  Per-bundle breakdown:")
        print(f"  {'Bundle':<20} {'Success':>8} {'Total':>6} {'Rate':>8}")
        print(f"  {'-'*20} {'-'*8} {'-'*6} {'-'*8}")
        for b in sorted(bundle_stats.keys()):
            s = bundle_stats[b]
            r = (s["success"] / s["total"] * 100) if s["total"] > 0 else 0
            print(f"  {b:<20} {s['success']:>8} {s['total']:>6} {r:>7.1f}%")

    print(f"\n{'='*60}\n")
    return {
        "total": total_tasks,
        "evaluated": evaluated,
        "success": success,
        "rate": rate,
        "per_bundle": bundle_stats,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="One-command KR benchmark: WebClaw → trajectory → WebJudge → score",
    )
    parser.add_argument("--config", default=str(CONFIG_PATH), help="Config file path")
    parser.add_argument("--task-ids", default="all", help="Comma-separated task ids or 'all'")
    parser.add_argument("--bundle", default=None, help="Filter by baryon_bundle slug")
    parser.add_argument("--domain", default=None, help="Filter by domain")
    parser.add_argument("--difficulty", default=None, help="Filter by difficulty (easy/medium/hard)")
    parser.add_argument("--limit", type=int, default=None, help="Max tasks to run")
    parser.add_argument("--skip-exec", action="store_true", help="Skip WebClaw execution (trajectories exist)")
    parser.add_argument("--skip-eval", action="store_true", help="Skip WebJudge evaluation")
    parser.add_argument("--output-dir", default=None, help="Override trajectories output dir")
    args = parser.parse_args()

    print(BANNER)

    cfg = load_config(Path(args.config))
    output_dir = args.output_dir or cfg.get("output_dir", "./data/kr/trajectories")

    tasks = load_tasks(
        task_ids=args.task_ids,
        bundle=args.bundle,
        domain=args.domain,
        difficulty=args.difficulty,
        limit=args.limit,
    )
    if not tasks:
        print("No tasks matched the filter.", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded {len(tasks)} KR tasks")
    if args.bundle:
        print(f"  Bundle: {args.bundle}")
    if args.domain:
        print(f"  Domain: {args.domain}")
    if args.difficulty:
        print(f"  Difficulty: {args.difficulty}")
    if args.limit:
        print(f"  Limit: {args.limit}")

    start_time = time.time()

    # Phase 1: Execute tasks via WebClaw
    if not args.skip_exec:
        ok = run_webclaw(cfg, tasks, output_dir)
        if not ok and not args.skip_eval:
            print("Execution failed. Use --skip-eval to abort.", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"\nSkipping WebClaw execution (--skip-exec)")
        print(f"Using existing trajectories in {output_dir}")

    # Phase 2: WebJudge evaluation
    eval_output = ""
    if not args.skip_eval:
        eval_output = run_eval(cfg, output_dir)
    else:
        print(f"\nSkipping WebJudge evaluation (--skip-eval)")
        eval_output = f"{output_dir}_result"

    # Phase 3: Score summary
    if eval_output:
        score = compute_score(eval_output, len(tasks))
        elapsed = time.time() - start_time
        print(f"Total elapsed: {elapsed:.0f}s ({elapsed/60:.1f}m)")
        # Write score summary to file
        score_path = Path(eval_output) / "score_summary.json"
        with open(score_path, "w", encoding="utf-8") as f:
            json.dump(score, f, ensure_ascii=False, indent=2)
        print(f"Score summary written to {score_path}")


if __name__ == "__main__":
    main()