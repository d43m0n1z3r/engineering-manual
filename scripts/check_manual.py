#!/usr/bin/env python3
"""Consistency checks for the Engineering Manual repository.

Stdlib-only checks intended for CI and local verification:
- manifest.json validity and listed files
- generated-artifact counts (skills, task cards, role cards)
- relative Markdown links
- task-card required sections and task-table/card consistency
- § section references resolve through XREF.md
- task registry schema, references, and dependency cycles
- checklist checkbox format and obvious secret patterns
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def markdown_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def check_manifest() -> None:
    path = ROOT / "manifest.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        fail(f"manifest.json is not valid JSON: {exc}")
        return
    for item in data.get("section_files", []):
        if not (ROOT / item).exists():
            fail(f"manifest.json lists missing file: {item}")


def check_counts() -> None:
    skills = list((ROOT / "skills").glob("[0-9][0-9]-*.md"))
    if len(skills) != 23:
        fail(f"expected 23 skill category files, found {len(skills)}")
    tasks = list(ROOT.glob("workflow/**/tasks/*.md"))
    if len(tasks) != 108:
        fail(f"expected 108 task cards, found {len(tasks)}")
    roles = [p for p in (ROOT / "agents" / "roles").glob("*.md") if p.name != "README.md"]
    if len(roles) != 12:
        fail(f"expected 12 role cards, found {len(roles)}")


def check_links() -> None:
    link_re = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in link_re.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            candidate = (ROOT / target.lstrip("/")) if target.startswith("/") else (path.parent / target).resolve()
            if not candidate.exists():
                fail(f"{rel(path)}: broken relative link -> {match.group(1)}")


REQUIRED_CARD_SECTIONS = [
    "Source task and objective",
    "Execution instructions",
    "Expected outputs",
    "Validation",
    "Required context and task instantiation",
    "Source table headings",
]
TASK_ID_RE = re.compile(r"^\|\s*((?:P\d{2}|X-KICKOFF)-T\d{2})\s*\|")


def check_task_cards() -> set[str]:
    cards = sorted(ROOT.glob("workflow/**/tasks/*.md"))
    card_ids = {p.stem for p in cards}
    for path in cards:
        text = path.read_text(encoding="utf-8")
        for section in REQUIRED_CARD_SECTIONS:
            if f"## {section}" not in text:
                fail(f"{rel(path)}: missing required section '## {section}'")
        if not text.splitlines() or not text.splitlines()[0].startswith(f"# {path.stem}"):
            fail(f"{rel(path)}: title does not start with task id {path.stem}")

    table_ids: dict[str, list[str]] = {}
    for path in sorted((ROOT / "workflow").rglob("*.md")):
        if "/tasks/" in f"/{path.parent.as_posix()}/" or path.parent.name == "tasks":
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            m = TASK_ID_RE.match(line.strip())
            if m:
                table_ids.setdefault(m.group(1), []).append(rel(path))

    for task_id, sources in table_ids.items():
        matches = list(ROOT.glob(f"workflow/**/tasks/{task_id}.md"))
        if len(matches) != 1:
            fail(f"task {task_id} from {sources} has {len(matches)} task cards")
            continue
        card_text = matches[0].read_text(encoding="utf-8")
        if not card_text.splitlines()[0].startswith(f"# {task_id}"):
            fail(f"{rel(matches[0])}: title does not start with task id {task_id}")

    for task_id in sorted(card_ids - set(table_ids)):
        fail(f"task card {task_id} has no source task-table row")
    for task_id in sorted(set(table_ids) - card_ids):
        fail(f"task-table row {task_id} has no task card")

    tasks_md = (ROOT / "TASKS.md").read_text(encoding="utf-8")
    for task_id in card_ids:
        if f"{task_id}](" not in tasks_md:
            fail(f"TASKS.md does not list task card {task_id}")
    return card_ids


def check_section_refs() -> None:
    xref = (ROOT / "XREF.md").read_text(encoding="utf-8")
    valid = set(re.findall(r"^\|\s*(§\d+\.\d+)\s*\|", xref, re.MULTILINE))
    skip = {"source/manual.md", "XREF.md", "CHANGELOG.md"}
    for path in markdown_files():
        r = rel(path)
        if r in skip:
            continue
        for match in re.finditer(r"§(\d+\.\d+)", path.read_text(encoding="utf-8")):
            if f"§{match.group(1)}" not in valid:
                fail(f"{r}: §{match.group(1)} is not mapped in XREF.md")


def check_registry(card_ids: set[str]) -> None:
    path = ROOT / "workflow" / "task-registry.json"
    if not path.exists():
        fail("workflow/task-registry.json is missing")
        return
    try:
        reg = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        fail(f"workflow/task-registry.json is not valid JSON: {exc}")
        return

    tasks = reg.get("tasks")
    if not isinstance(tasks, list):
        fail("task-registry.json: 'tasks' must be a list")
        return
    reg_ids = {t.get("id") for t in tasks}
    if reg_ids != card_ids:
        fail(f"task-registry.json ids do not match task cards (registry={len(reg_ids)}, cards={len(card_ids)})")

    gates = set((reg.get("gates") or {}).keys())
    skills = set((reg.get("skill_categories") or {}).keys())
    required = {"id", "phase", "role", "roles", "skills", "depends_on", "gate_required", "feeds_gates", "validation", "card", "source"}
    graph: dict[str, list[str]] = {}
    for task in tasks:
        tid = task.get("id", "<missing>")
        missing = required - set(task)
        if missing:
            fail(f"task-registry.json {tid}: missing fields {sorted(missing)}")
            continue
        for field in ("depends_on", "gate_required", "feeds_gates"):
            for ref in task[field]:
                if field == "depends_on" and ref not in reg_ids:
                    fail(f"task-registry.json {tid}: unknown depends_on {ref}")
                if field in {"gate_required", "feeds_gates"} and ref not in gates:
                    fail(f"task-registry.json {tid}: unknown gate {ref}")
        for skill in task["skills"]:
            if str(skill) not in skills:
                fail(f"task-registry.json {tid}: unknown skill category {skill}")
        if not (ROOT / task["card"]).exists():
            fail(f"task-registry.json {tid}: missing card {task['card']}")
        if task.get("source") and not (ROOT / task["source"]).exists():
            fail(f"task-registry.json {tid}: missing source {task['source']}")
        role_path = ROOT / "agents" / "roles" / f"{task['role']}.md"
        if not role_path.exists():
            fail(f"task-registry.json {tid}: unknown role {task['role']}")
        graph[tid] = list(task["depends_on"])

    # Cycle detection (Kahn). Only registry tasks are nodes; external refs were already flagged.
    indegree = {tid: 0 for tid in graph}
    for tid, deps in graph.items():
        for dep in deps:
            if dep in indegree:
                indegree[tid] += 1
    queue = [tid for tid, deg in indegree.items() if deg == 0]
    seen = 0
    while queue:
        node = queue.pop()
        seen += 1
        for tid, deps in graph.items():
            if node in deps:
                indegree[tid] -= 1
                if indegree[tid] == 0:
                    queue.append(tid)
    if seen != len(graph):
        fail("task-registry.json: dependency graph contains a cycle")


def check_checklists_and_secrets() -> None:
    for path in sorted((ROOT / "checklists").glob("*.md")):
        if path.name == "README.md":
            continue
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.count("- [ ]") > 1 or line.count("- [x]") > 1 or line.count("- [X]") > 1:
                fail(f"{rel(path)}:{lineno}: multiple checklist items on one line")

    secret_patterns = [
        r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
        r"AKIA[0-9A-Z]{16}",
        r"ghp_[0-9A-Za-z]{30,}",
        r"xox[baprs]-[0-9A-Za-z-]{10,}",
        r"sk-[0-9A-Za-z]{20,}",
    ]
    for path in markdown_files():
        if rel(path) == "source/manual.md":
            continue
        text = path.read_text(encoding="utf-8")
        for pat in secret_patterns:
            if re.search(pat, text):
                fail(f"{rel(path)}: possible secret pattern {pat}")


def main() -> int:
    check_manifest()
    check_counts()
    card_ids = check_task_cards()
    check_links()
    check_section_refs()
    check_registry(card_ids)
    check_checklists_and_secrets()

    if errors:
        print(f"FAILED: {len(errors)} issue(s)")
        for err in errors[:200]:
            print(f"- {err}")
        if len(errors) > 200:
            print(f"... and {len(errors) - 200} more")
        return 1
    print("OK: manual consistency checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
