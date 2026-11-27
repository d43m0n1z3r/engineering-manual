#!/usr/bin/env python3
"""Compute READY tasks from workflow/task-registry.json.

READY means: all depends_on tasks are verified, all gate_required gates are
approved, and the task is not already verified or claimed. This is a
deterministic helper for the Orchestrator; it does not replace ledger state or
human approvals.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "workflow" / "task-registry.json"


def csv_set(value: str | None) -> set[str]:
    if not value:
        return set()
    return {item.strip() for item in value.split(",") if item.strip()}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verified", default="", help="comma-separated VERIFIED task IDs")
    ap.add_argument("--claimed", default="", help="comma-separated claimed/IN_PROGRESS task IDs")
    ap.add_argument("--approved-gates", default="", help="comma-separated approved gate IDs, e.g. G0,G1")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args()

    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    tasks = reg.get("tasks", [])
    by_id = {t["id"]: t for t in tasks}

    verified = csv_set(args.verified)
    claimed = csv_set(args.claimed)
    approved_gates = csv_set(args.approved_gates)

    ready: list[dict] = []
    blocked: list[dict] = []

    for task in tasks:
        tid = task["id"]
        if tid in verified or tid in claimed:
            continue
        missing_deps = [d for d in task.get("depends_on", []) if d not in verified]
        missing_gates = [g for g in task.get("gate_required", []) if g not in approved_gates]
        if not missing_deps and not missing_gates:
            ready.append(task)
        else:
            blocked.append({
                "id": tid,
                "missing_deps": missing_deps,
                "missing_gates": missing_gates,
                "human_approval": task.get("human_approval", ""),
            })

    if args.json:
        print(json.dumps({"ready": [t["id"] for t in ready], "blocked": blocked}, indent=2))
        return 0

    print(f"READY ({len(ready)}):")
    for task in ready:
        note = f"  human_approval={task.get('human_approval')}" if task.get("human_approval") else ""
        print(f"- {task['id']} {task.get('name', '')}{note}")
    print(f"\nBLOCKED ({len(blocked)}):")
    for item in blocked[:200]:
        reasons = []
        if item["missing_deps"]:
            reasons.append("deps=" + ",".join(item["missing_deps"]))
        if item["missing_gates"]:
            reasons.append("gates=" + ",".join(item["missing_gates"]))
        if item["human_approval"]:
            reasons.append(f"human={item['human_approval']}")
        print(f"- {item['id']}: {'; '.join(reasons)}")
    if len(blocked) > 200:
        print(f"... and {len(blocked) - 200} more")
    return 0


if __name__ == "__main__":
    sys.exit(main())
