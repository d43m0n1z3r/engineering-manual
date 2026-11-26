# Engineering Manual Index

This repository was generated from `source/manual.md`. The source is retained
for audit and recovery. Review `REPORT.md` before operational use.

## Context loading

Load the documents needed for the current task. Keep context focused, but do
not omit a required security control, approval, gate, or dependency simply to
meet a file-count limit.

### For a typical task

1. [Agent entry point](AGENTS.md)
2. The relevant file under [agents/roles/](agents/roles/)
3. The relevant phase README under [workflow/phases/](workflow/phases/)
4. The task card under that phase's `tasks/` directory
5. The relevant skill categories under [skills/](skills/)
6. Applicable gates, standards, checklists, and templates

The [task index](TASKS.md) lists generated task cards.

### Situation-specific references

| Situation | Open |
|---|---|
| Starting or instantiating a task | [Task schema](agents/protocol/01-task-schema.md) |
| Recording evidence | [Evidence standard](core/04-evidence-standard.md) |
| Requesting a handoff | [Handoff protocol](agents/protocol/06-handoff.md) |
| Human approval | [Human approval matrix](agents/protocol/08-human-approval.md) |
| Offensive security work | [Offensive security](workflow/phases/06-security/B-offensive-security.md) and [RoE template](templates/roe.md) |
| Gate review | Relevant file under [workflow/gates/](workflow/gates/) |
| Choosing technology | [Selection procedure](tools/selection-procedure.md) and [landscape](tools/landscape.md) |
| Security finding | [Vulnerability template](templates/vulnerability.md) |
| Incident | [Incident response](standards/operations/incident-response.md) |
| Release | [Release phase](workflow/phases/09-release/README.md) and [release checklist](checklists/release-readiness.md) |
| Querying or refreshing agent memory (Graphify) | [Context ledger](agents/protocol/04-context-ledger.md) and [MEMORY.md](ledger-template/MEMORY.md) |

## Directory map

| Directory | Purpose |
|---|---|
| `core/` | Non-negotiables, principles, classifications, evidence |
| `workflow/` | SDLC phases, task cards, gates, and dependencies |
| `agents/` | Roles, permissions, human authorities, execution protocol |
| `skills/` | Competency taxonomy and proficiency levels |
| `standards/` | Testing, CI/CD, operations, documentation, improvement |
| `tools/` | Technology and tool selection |
| `templates/` | Reusable evidence, RoE, incident, ADR, and other templates |
| `checklists/` | Definitions of done and engineering checklists |
| `ledger-template/` | Starter project state and traceability files |
| `source/` | Unmodified source manual |
| `XREF.md` | Map of original numbered sections to generated files |

## Original references

The generated files preserve references such as “Part 8” and “§2.3” from the
source manual. They are not automatically rewritten. Use [XREF.md](XREF.md),
the directory map above, or search `source/manual.md`.

## Conflicts

Generated files preserve the source rather than resolving contradictions.
Escalate substantive conflicts to the appropriate human authority. Do not
silently choose whichever rule is more convenient.
