#!/usr/bin/env python3
"""Print distribution statistics for the KR benchmark tasks."""
import collections
import json
import os

KR_TASKS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data", "kr", "tasks",
)


def main():
    tasks = []
    for fn in sorted(os.listdir(KR_TASKS_DIR)):
        if not fn.endswith(".json"):
            continue
        with open(os.path.join(KR_TASKS_DIR, fn), encoding="utf-8") as f:
            tasks.append(json.load(f))

    print(f"Total KR tasks: {len(tasks)}")
    print()

    print("=== Domain distribution ===")
    for domain, count in collections.Counter(t["domain"] for t in tasks).most_common():
        print(f"  {domain:<25} {count}")

    print()
    print("=== Difficulty distribution ===")
    diff_order = ["easy", "medium", "hard"]
    for diff in diff_order:
        count = sum(1 for t in tasks if t["difficulty"] == diff)
        print(f"  {diff:<10} {count}")

    print()
    sites = collections.Counter(t["website"] for t in tasks)
    print(f"=== Website distribution ({len(sites)} unique sites) ===")
    for site, count in sites.most_common():
        print(f"  {count}x  {site}")

    print()
    print("=== Reference length stats ===")
    lengths = [t["reference_length"] for t in tasks]
    print(f"  min={min(lengths)}  max={max(lengths)}  avg={sum(lengths)/len(lengths):.1f}")


if __name__ == "__main__":
    main()