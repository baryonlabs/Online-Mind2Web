#!/usr/bin/env python3
"""Generate deterministic task_id hashes for KR benchmark tasks.

Usage:
    python script/gen_kr_task_ids.py            # print all tasks with ids
    python script/gen_kr_task_ids.py --write     # write data/kr/tasks/<task_id>.json
"""
import argparse
import hashlib
import json
import os

from kr_tasks import KR_TASKS

KR_TASKS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data", "kr", "tasks",
)


def make_task_id(task_description: str, website: str) -> str:
    raw = f"{website}|{task_description}"
    return hashlib.md5(raw.encode("utf-8")).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true",
                        help="write individual task json files")
    args = parser.parse_args()

    seen_ids = set()
    for task in KR_TASKS:
        tid = make_task_id(task["task_description"], task["website"])
        if tid in seen_ids:
            raise ValueError(f"Duplicate task_id {tid} for: {task['task_description']}")
        seen_ids.add(tid)
        task["task_id"] = tid

    if args.write:
        os.makedirs(KR_TASKS_DIR, exist_ok=True)
        for task in KR_TASKS:
            path = os.path.join(KR_TASKS_DIR, f"{task['task_id']}.json")
            with open(path, "w", encoding="utf-8") as f:
                json.dump(task, f, ensure_ascii=False, indent=2)
        print(f"Wrote {len(KR_TASKS)} task files to {KR_TASKS_DIR}")
    else:
        print(json.dumps(KR_TASKS, ensure_ascii=False, indent=2))
        print(f"\nTotal: {len(KR_TASKS)} tasks", file=os.sys.stderr)


if __name__ == "__main__":
    main()