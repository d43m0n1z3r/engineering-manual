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
| Agent tooling, MCP servers, or external model/tool endpoints | [Agent ecosystem threat model](agents/agent-threat-model.md) and [human approval matrix](agents/protocol/08-human-approval.md) |
| Gate review | Relevant file under [workflow/gates/](workflow/gates/) |
| Choosing technology | [Selection procedure](tools/selection-procedure.md) and [landscape](tools/landscape.md) |
| Security finding | [Vulnerability template](templates/vulnerability.md) |
| Incident | [Incident response](standards/operations/incident-response.md) |
| Release | [Release phase](workflow/phases/09-release/README.md) and [release checklist](checklists/release-readiness.md) |
| Querying or refreshing agent memory (Graphify) | [Context ledger](agents/protocol/04-context-ledger.md) and [MEMORY.md](ledger-template/MEMORY.md) |
| Defect or CCR handling | [CCR template](templates/ccr.md), [defect register](ledger-template/DEFECTS.md), [defect handling](standards/testing/defect-handling.md) |
| Test thresholds | [Testing strategy and thresholds](standards/testing/strategy-and-thresholds.md) |
| Ledger initialization | [Ledger template](ledger-template/README.md) and [X-KICKOFF-T03](workflow/kickoff/tasks/X-KICKOFF-T03.md) |
| Definition of done | [Definition of Done](checklists/definition-of-done.md) |
| CI/CD architecture | [Pipeline architecture](standards/cicd/pipeline-architecture.md) |
| Agent capability validation | [Role skill minimums](skills/role-minimums.md) and the Agent Capability Register in [documentation standard](standards/documentation.md) |
| Template coverage | [Template catalog](templates/README.md) |
| Task orchestration | [Task registry](workflow/task-registry.json), [registry doc](workflow/task-registry.md), [dependencies](workflow/state-machine/dependencies.md) |
| Repository consistency checks | [check_manual.py](scripts/check_manual.py), [build_task_registry.py](scripts/build_task_registry.py), [scripts README](scripts/README.md) |
| Manual amendments and governance | [CONTRIBUTING.md](CONTRIBUTING.md), [AMENDMENT-PROCESS.md](AMENDMENT-PROCESS.md), [CHANGELOG.md](CHANGELOG.md) |

## Directory map

| Directory | Purpose |
|---|---|
| `core/` | Non-negotiables, principles, classifications, evidence |
| `workflow/` | SDLC phases, task cards, gates, dependencies, and the task registry |
| `agents/` | Roles, permissions, human authorities, agent threat model, execution protocol |
| `skills/` | Competency taxonomy and proficiency levels |
| `standards/` | Testing, CI/CD, operations, documentation, improvement |
| `tools/` | Technology and tool selection |
| `templates/` | Reusable evidence, RoE, incident, ADR, CCR, and other templates |
| `checklists/` | Definitions of done and engineering checklists |
| `ledger-template/` | Starter project state and traceability files |
| `scripts/` | Consistency checks and the task-registry generator |
| `.github/` | CI workflow for manual checks |
| `source/` | Frozen original generation input |
| `XREF.md` | Map of original numbered sections to generated files |

## Original references

The generated files preserve references such as “Part 8” and “§2.3” from the
source manual. They are not automatically rewritten. Use [XREF.md](XREF.md),
the directory map above, or search `source/manual.md`.

## Conflicts

Generated files preserve the source rather than resolving contradictions.
Escalate substantive conflicts to the appropriate human authority. Do not
silently choose whichever rule is more convenient.
