# Engineering Manual

> An operational standard operating procedure (SOP) for AI agents and human
> engineers that design, build, secure, test, deploy, and operate software.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.3.0-blue.svg)](manifest.json)
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
- **Agent memory stays current.** When Graphify is configured, agents query
  the knowledge graph before editing and refresh it after every addition,
  change, or fix — alongside the ledger, never instead of it.
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
| [`TASKS.md`](TASKS.md) | Task-card index (108 cards) |
| [`workflow/task-registry.json`](workflow/task-registry.json) | Machine-readable task/gate registry |
| [`XREF.md`](XREF.md) | Original section cross-reference |
| [`REPORT.md`](REPORT.md) | Generation report and known limitations |
| [`CHANGELOG.md`](CHANGELOG.md) | Living-repository change log |
| [`references.md`](references.md) | Standards and references cited |
| [`manifest.json`](manifest.json) | Provenance and generated-file manifest |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution and amendment rules |
| [`SECURITY.md`](SECURITY.md) | Security reporting |
| [`CODEOWNERS`](CODEOWNERS) | Review ownership |
| [`AMENDMENT-PROCESS.md`](AMENDMENT-PROCESS.md) | Manual amendment governance |
| `core/` | Non-negotiables, principles, data classifications, evidence standard |
| `workflow/` | SDLC phases, task cards, gates, state machine, kickoff, task registry |
| `agents/` | Role cards, permission tiers, human authorities, agent threat model, execution protocol |
| `skills/` | Competency taxonomy: 23 skill categories with proficiency levels |
| `standards/` | Testing, CI/CD, operations, documentation, improvement standards |
| `tools/` | Technology selection procedure, landscape, and archetypes |
| `templates/` | Template catalog: evidence, gate dossier, RoE, ADR, vulnerability, incident, PR, CCR |
| `checklists/` | Definitions of done and per-domain engineering checklists |
| `ledger-template/` | Starter project state and traceability files for new projects |
| `scripts/` | Repository consistency checks and the task-registry generator |
| `.github/` | CI checks for this manual |
| `source/` | The frozen original generation input, preserved for audit |

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
- `source/manual.md` is the frozen original generation input preserved for
  audit, not a live mirror of this repository. Post-generation changes are
  tracked in `CHANGELOG.md`; recovering from `source/manual.md` restores the
  generation baseline only.
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
