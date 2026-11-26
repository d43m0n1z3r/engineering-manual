# Engineering Manual

> An operational standard operating procedure (SOP) for AI agents and human
> engineers that design, build, secure, test, deploy, and operate software.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](manifest.json)
[![Phases](https://img.shields.io/badge/SDLC%20phases-11-orange.svg)](workflow/phases/)
[![Tasks](https://img.shields.io/badge/task%20cards-108-orange.svg)](TASKS.md)
[![Roles](https://img.shields.io/badge/agent%20roles-12-purple.svg)](agents/roles/)
[![Gates](https://img.shields.io/badge/quality%20gates-G0--G10-red.svg)](workflow/gates/)
[![Security](https://img.shields.io/badge/security-integrated-e11d48.svg)](workflow/phases/06-security/)
[![Docs](https://img.shields.io/badge/format-Markdown-083fa1.svg)](#repository-layout)

---

## Why this exists

Most "AI does the coding" setups fail for the same reason: no process. Work
starts mid-stream, nobody knows what's done, security is an afterthought, and
completion is declared by vibes.

The Engineering Manual fixes that. It turns software delivery into a
**predictable, auditable, and secure** pipeline:

- **Phases (01–11)** break work into stages with defined deliverables.
- **108 task cards** are atomic work units with explicit inputs, outputs,
  validation, and failure handling.
- **Gates (G0–G10)** are mandatory checkpoints — no gate, no progress.
- **12 agent roles** are permission-scoped actors: orchestrator, architect,
  developers, QA, security engineer, penetration tester, and more.
- **Evidence is the only currency of completion.** A task is not done until its
  evidence is recorded.
- **Humans approve** high-impact, irreversible, or out-of-scope actions —
  including all offensive security testing, which requires written
  authorization and a signed Rules of Engagement (`templates/roe.md`).

Security isn't a phase that happens late. It's embedded in every stage —
requirements, architecture, implementation, testing, deployment, release,
operations, and improvement.

## Repository layout

| Path | Contents |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Entry point and core obligations for agents |
| [`INDEX.md`](INDEX.md) | Context-loading guide and directory map |
| `core/` | Non-negotiables, principles, data classifications, evidence standard |
| `workflow/` | SDLC phases, task cards, gates, state machine, kickoff |
| `agents/` | Role cards, permission tiers, human authorities, execution protocol |
| `skills/` | Competency taxonomy: 23 skill categories with proficiency levels |
| `standards/` | Testing, CI/CD, operations, documentation, improvement standards |
| `tools/` | Technology selection procedure, landscape, and archetypes |
| `templates/` | Evidence, gate dossier, RoE, ADR, vulnerability, incident, PR templates |
| `checklists/` | Definitions of done and per-domain engineering checklists |
| `ledger-template/` | Starter project state and traceability files for new projects |
| `source/` | The original manual, preserved unmodified for audit |

## Quick start

1. Read [`AGENTS.md`](AGENTS.md), then [`INDEX.md`](INDEX.md).
2. To run a project under this manual, copy `ledger-template/` into your
   project and follow the task lifecycle in `agents/protocol/`.
3. Find any task by ID in [`TASKS.md`](TASKS.md).
4. New to a phase? Start at `workflow/phases/` and work through the README in
   each phase directory.

## Provenance and caveats

This repository was **generated from a single source manual**
(`source/manual.md`, preserved verbatim for audit and recovery).

- Task and role cards are **derived convenience views**; the authoritative
  content remains in the phase files and `source/`.
- The files preserve the source rather than resolving contradictions —
  escalate conflicts to the appropriate human authority.
- Original cross-references (e.g. "Part 8", "§2.3") are preserved, not rewritten;
  use [`XREF.md`](XREF.md) to resolve them.
- Referenced standards editions may age — verify current editions before
  relying on them ([`references.md`](references.md) lists what's cited).

See [`REPORT.md`](REPORT.md) for the full generation report and known
limitations **before operational use**.

## License

[MIT](LICENSE) — use it, fork it, adapt it. Attribution appreciated.

---

<p align="center"><sub>Built for agents. Enforced by humans.</sub></p>
