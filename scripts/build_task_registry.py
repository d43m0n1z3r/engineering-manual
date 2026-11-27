#!/usr/bin/env python3
"""Build workflow/task-registry.json from the task cards and phase metadata.

The registry is a machine-readable operationalization of workflow/state-machine/
dependencies.md. Task cards remain the authoritative task text; this file adds
orchestration fields (depends_on, gate_required, feeds_gates, role, skills).
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "workflow" / "task-registry.json"

PHASE_ORDER = ["X-KICKOFF"] + [f"P{i:02d}" for i in range(1, 12)]

# phase_id -> (workflow dir, lead role, involved agent roles, skill categories)
PHASES = {
    "X-KICKOFF": (
        "workflow/kickoff",
        "orchestrator",
        ["orchestrator"],
        [4, 23],
    ),
    "P01": (
        "workflow/phases/01-discovery-requirements",
        "project-analyst",
        ["project-analyst", "software-architect", "security-engineer", "technical-reviewer"],
        [4, 9, 14, 23],
    ),
    "P02": (
        "workflow/phases/02-architecture",
        "software-architect",
        ["software-architect", "security-engineer", "database-engineer", "devops-engineer", "technical-reviewer"],
        [7, 8, 9, 12, 14, 19],
    ),
    "P03": (
        "workflow/phases/03-ui-ux-frontend",
        "frontend-developer",
        ["ui-ux-engineer", "frontend-developer", "security-engineer", "qa-engineer", "technical-reviewer"],
        [5, 14, 21, 22, 23],
    ),
    "P04": (
        "workflow/phases/04-backend-api",
        "backend-developer",
        ["backend-developer", "security-engineer", "database-engineer", "qa-engineer", "technical-reviewer"],
        [2, 3, 4, 6, 8, 14, 19, 22],
    ),
    "P05": (
        "workflow/phases/05-database",
        "database-engineer",
        ["database-engineer", "backend-developer", "security-engineer", "devops-engineer"],
        [7, 12, 14, 19, 22],
    ),
    "P06": (
        "workflow/phases/06-security",
        "security-engineer",
        ["security-engineer", "penetration-tester", "devops-engineer", "technical-reviewer"],
        [11, 14, 15, 16, 17, 18, 19, 20],
    ),
    "P07": (
        "workflow/phases/07-testing-qa",
        "qa-engineer",
        ["qa-engineer", "frontend-developer", "backend-developer", "database-engineer", "security-engineer", "devops-engineer"],
        [4, 21, 22],
    ),
    "P08": (
        "workflow/phases/08-devops-cicd",
        "devops-engineer",
        ["devops-engineer", "security-engineer", "software-architect", "technical-reviewer"],
        [10, 11, 12, 13, 19, 20],
    ),
    "P09": (
        "workflow/phases/09-release",
        "devops-engineer",
        ["devops-engineer", "orchestrator", "technical-reviewer", "security-engineer", "qa-engineer"],
        [12, 13, 14, 21, 23],
    ),
    "P10": (
        "workflow/phases/10-operations",
        "devops-engineer",
        ["devops-engineer", "security-engineer", "backend-developer", "database-engineer", "orchestrator"],
        [10, 11, 12, 13, 17, 18, 20, 22, 23],
    ),
    "P11": (
        "workflow/phases/11-improvement",
        "project-analyst",
        ["project-analyst", "software-architect", "security-engineer", "devops-engineer", "qa-engineer", "technical-reviewer"],
        [4, 9, 14, 21, 22, 23],
    ),
}

TASK_COUNTS = {
    "X-KICKOFF": 4,
    "P01": 9, "P02": 9, "P03": 9, "P04": 10, "P05": 9, "P06": 13,
    "P07": 9, "P08": 11, "P09": 8, "P10": 9, "P11": 8,
}

BUILD_PHASES = {"P03", "P04", "P05"}


def phase_task_ids(phase: str) -> list[str]:
    return [f"{phase}-T{i:02d}" for i in range(1, TASK_COUNTS[phase] + 1)]


def section(text: str, heading: str) -> str:
    match = re.search(rf"^## {re.escape(heading)}\s*$", text, re.MULTILINE)
    if not match:
        return ""
    rest = text[match.end():]
    nxt = re.search(r"^## ", rest, re.MULTILINE)
    return (rest[: nxt.start()] if nxt else rest).strip()


def parse_card(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    task_id = path.stem
    title = text.splitlines()[0].strip()
    name = title.split(" — ", 1)[-1].strip() if " — " in title else task_id
    gen = re.search(r"Generated from \[[^\]]+\]\(([^)]+)\)", text)
    source = ""
    if gen:
        source = (path.parent / gen.group(1)).resolve()
    return {
        "id": task_id,
        "name": name,
        "outputs": section(text, "Expected outputs"),
        "validation": section(text, "Validation"),
        "card": path.relative_to(ROOT).as_posix(),
        "source": source.relative_to(ROOT).as_posix() if source else "",
    }


def orchestration(task_id: str) -> dict:
    phase = "X-KICKOFF" if task_id.startswith("X-KICKOFF") else task_id.split("-")[0]
    seq = int(task_id.rsplit("-T", 1)[1])
    deps: list[str] = []
    gates: list[str] = []
    feeds: list[str] = []
    human = ""

    if phase == "X-KICKOFF":
        feeds = ["G0"]
        if task_id == "X-KICKOFF-T01":
            human = "Sponsor and named gate approvers"
        elif task_id == "X-KICKOFF-T02":
            human = "Security review"
        elif task_id == "X-KICKOFF-T04":
            human = "Security Authority"
    elif phase == "P01":
        gates = ["G0"]
        if seq == 9:
            deps = phase_task_ids("P01")[:8]
            feeds = ["G1"]
        else:
            deps = phase_task_ids("X-KICKOFF")
    elif phase == "P02":
        gates = ["G1"]
        if seq == 9:
            deps = phase_task_ids("P02")[:8]
            feeds = ["G2", "G3", "G4"]
        elif task_id == "P02-T07":
            deps = ["P01-T09", "P02-T03", "P02-T06"]
        else:
            deps = ["P01-T09"]
    elif phase in BUILD_PHASES:
        gates = ["G2", "G3", "G4"]
        last = TASK_COUNTS[phase]
        if seq == last:
            deps = phase_task_ids(phase)[: last - 1]
            feeds = {"P03": ["G6"], "P04": ["G6", "G7"], "P05": ["G6"]}[phase]
        elif phase == "P04" and task_id == "P04-T04":
            deps = ["P04-T02", "P05-T02"]
        elif phase == "P05" and seq >= 3:
            deps = ["P02-T09", "P05-T02"]
        else:
            deps = ["P02-T09"]
    elif phase == "P06":
        if seq <= 3:
            deps = ["P02-T09"]
            gates = ["G3"]
        elif seq == 4:
            deps = ["P08-T05", "X-KICKOFF-T04"]
            gates = ["G0"]
            human = "Security Authority and system owner"
        elif seq <= 10:
            deps = [phase_task_ids("P06")[seq - 2]]
            if seq == 9:
                human = "per finding class"
            if seq == 10:
                feeds = ["G7"]
        else:
            deps = ["P02-T09"]
            gates = ["G3"]
            if seq == 13:
                feeds = ["G7"]
    elif phase == "P07":
        deps = ["P03-T09", "P04-T10", "P05-T09"]
        if task_id == "P07-T05":
            deps.append("P08-T05")
        if seq == 9:
            feeds = ["G6"]
    elif phase == "P08":
        gates = ["G2", "G3", "G4"]
        if seq == 11:
            deps = phase_task_ids("P08")[:10]
            feeds = ["G8"]
        else:
            deps = ["P02-T09"]
    elif phase == "P09":
        if seq == 1:
            deps = ["P07-T09", "P06-T10", "P08-T11"]
            gates = ["G6", "G7", "G8"]
        elif seq == 2:
            deps = ["P09-T01"]
        elif seq == 3:
            deps = ["P09-T02"]
            human = "Security Authority"
        elif seq == 4:
            deps = ["P09-T03"]
        elif seq == 5:
            deps = ["P09-T04"]
            gates = ["G9"]
            human = "Release Authority"
        elif seq == 6:
            deps = ["P09-T05"]
        elif seq == 7:
            deps = ["P09-T06"]
        else:
            deps = ["P09-T05", "P09-T06", "P09-T07"]
            feeds = ["G10"]
            human = "Release Authority"
    elif phase == "P10":
        deps = ["P09-T08"]
        gates = ["G10"]
    elif phase == "P11":
        deps = ["P10-T09"]

    return {"depends_on": deps, "gate_required": gates, "feeds_gates": feeds, "human_approval": human}


def parse_gate(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    title = text.splitlines()[0].strip().lstrip("# ").strip()
    def row(label: str) -> str:
        m = re.search(rf"^\| {re.escape(label)} \| (.*?) \|$", text, re.MULTILINE)
        return m.group(1).strip() if m else ""
    return {
        "file": path.relative_to(ROOT).as_posix(),
        "title": title,
        "entry": row("Entry"),
        "approval_authority": row("Approval authority"),
    }


def skill_categories() -> dict[str, dict]:
    cats = {}
    for path in sorted((ROOT / "skills").glob("[0-9][0-9]-*.md")):
        num = int(path.name[:2])
        heading = next((ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.startswith("#")), "")
        title = heading.lstrip("#").strip()
        cats[str(num)] = {"file": path.relative_to(ROOT).as_posix(), "title": title}
    return cats


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if the registry is stale")
    args = ap.parse_args()

    cards = []
    for phase, (wdir, *_rest) in PHASES.items():
        for path in sorted((ROOT / wdir / "tasks").glob("*.md")):
            cards.append((phase, path))

    tasks = []
    for phase, path in cards:
        task_id = path.stem
        if not task_id.startswith(phase):
            raise SystemExit(f"task id {task_id} does not match phase {phase} in {path}")
        entry = parse_card(path)
        wdir, _lead, roles, skills = PHASES[phase]
        orch = orchestration(task_id)
        lead = _lead
        if phase == "P03" and int(task_id.rsplit("-T", 1)[1]) <= 3:
            lead = "ui-ux-engineer"
        if phase == "P06" and task_id in {"P06-T05", "P06-T06", "P06-T07", "P06-T08", "P06-T09"}:
            lead = "penetration-tester" if task_id != "P06-T06" else "security-engineer"
        entry.update({
            "phase": phase,
            "phase_dir": wdir,
            "role": lead,
            "roles": roles,
            "skills": skills,
            **orch,
        })
        tasks.append(entry)

    order = {pid: i for i, pid in enumerate(PHASE_ORDER)}
    tasks.sort(key=lambda t: (order[t["phase"]], t["id"]))

    manual_version = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8")).get("manual_version", "0.0.0")
    registry = {
        "version": manual_version,
        "generated_by": "scripts/build_task_registry.py",
        "generated_from": "workflow/**/tasks/*.md plus curated orchestration metadata in this script",
        "semantics": {
            "depends_on": "hard task dependencies; a task is READY only when all listed tasks are VERIFIED",
            "gate_required": "gates that must be approved before the task may be claimed",
            "feeds_gates": "gates the task's verified output is submitted to; gate entry rules still apply",
            "role": "primary accountable agent role (slug under agents/roles/)",
            "roles": "agent roles involved in the phase",
            "skills": "Part 5 category numbers; see skill_categories for files/titles",
            "human_approval": "human approval required in addition to any gate, when stated by the manual",
        },
        "skill_categories": skill_categories(),
        "gates": {p.stem: parse_gate(p) for p in sorted((ROOT / "workflow" / "gates").glob("G*.md"))},
        "tasks": tasks,
    }

    rendered = json.dumps(registry, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != rendered:
            print("workflow/task-registry.json is stale; run scripts/build_task_registry.py")
            return 1
        print("workflow/task-registry.json is up to date")
        return 0

    OUT.write_text(rendered, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} with {len(tasks)} tasks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
