# Changelog

All notable changes to the Engineering Manual are documented here. The
`engineering-manual/` directory is the living repository — changes land there
continuously under `[Unreleased]`. A version number is bumped and a dated
section is added only when a release is cut; versioned snapshots live in
sibling directories (`engineering-manual-X.Y.Z/`).

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Deep specification pass across agents, checklists, core, ledger template,
  skills, standards, tools, workflow, scripts, and source provenance:
  - `agents/operating-model.md` and `agents/tooling-governance.md` for agent
    roles, permissions, MCP/plugin/hook vetting, egress, and change detection.
  - Expanded agent threat model, permission tiers, human authorities, protocol
    dependency/approval/logging/parallelization/prohibited-behavior detail.
  - New checklists for agent ecosystem, gate dossier, ledger integrity, supply
    chain, and data protection; expanded checklist index and usage rules.
  - Expanded data classification/handling, evidence storage/retention/integrity,
    document control, and non-negotiable interpretation notes.
  - Ledger template registers and READMEs now include status values, ID formats,
    review rules, and restricted-storage handling.
  - `skills/assessment-rubric.md` plus expanded skills README and role-minimums
    validation evidence requirements.
  - `standards/cicd/supply-chain.md` and `standards/operations/agent-operations.md`;
    expanded security validation methods for agentic/MCP/data-egress risks.
  - `workflow/gates/review-procedure.md` and `workflow/state-machine/orchestration-runbook.md`;
    dependency note pointing to the machine-readable registry.
  - `scripts/task_readiness.py` for deterministic READY-task computation.
  - `source/README.md` clarifying frozen provenance.

## [1.3.0] - 2026-11-27

### Added

- Agent ecosystem threat model and controls for agent skills, MCP servers,
  plugins, hooks, tool-output poisoning, confused deputy actions, data egress
  to external model/tool endpoints, credential persistence, ledger tampering,
  and goal misgeneralization.
- Process profile recording at X-KICKOFF-T01/G0 for pre-authorized rigor
  tailoring without waiving evidence, authorization, or ★ security criteria.
- Ledger registers for defects, incidents, and restricted vulnerabilities;
  evidence governance for storage class, retention, UTC timestamps, and
  integrity protection; and a deliverable template coverage catalog.
- Machine-readable task/gate registry (`workflow/task-registry.json`) with a
  generator and consistency checks; repository CI for manual checks; expanded
  navigation/index coverage; and skill-category links in phase READMEs.
- Repository governance files (`CONTRIBUTING.md`, `SECURITY.md`, `CODEOWNERS`,
  `AMENDMENT-PROCESS.md`), the Graphify `graphify-out/` output policy, and
  Roles/Skills metadata for phases 09–11.

### Fixed

- Reformatted all files in `checklists/` so each checklist item renders as
  its own Markdown line (previously multiple `- [ ]` items were crammed onto
  single lines and rendered as run-on text in previews).
- Clarified `source/manual.md` provenance as the frozen generation input and
  added manifest version/source-hash/provenance fields.
- Corrected stale or ambiguous references (`§4.6.B`, `Security (4.14)`,
  `§P05-T08`, `§P01-T06`, `§20`, and `§Gate-bypass policy`) and expanded
  `XREF.md` for unnumbered sections and generated artifacts.
- Aligned kickoff ledger initialization with `ledger-template/`, aligned the
  evidence type list with §2.4, and converted the code-review checklist to
  checkboxes.
- Standardized `skills/role-minimums.md` to skill category/row references,
  clarified ledger bootstrap for projects versus this manual repository, and
  defined the manual fingerprint used by load receipts.

## [1.2.0] - 2026-11-27

### Added

- **Graphify as agent memory.** When the project uses
  [Graphify](https://github.com/Graphify-Labs/graphify), agents MUST query the
  knowledge graph before editing and refresh it after every addition, change,
  or fix (`graphify . --update`, or the configured `--watch` / post-commit
  hook) — in the same change set as the ledger update. The graph complements,
  never replaces, the ledger.
- New `ledger-template/MEMORY.md` starter file defining the recall/refresh
  rules, graph location, install notes, and the no-secrets constraint.
- Agent-memory rows/fields in the context ledger, handoff packet, boot
  sequence, and kick-off task X-KICKOFF-T03 (which now also initializes
  `graphify-out/`).
- Self-check item and task-level DoD item requiring the graph refresh.

### Changed

- `AGENTS.md` obligation 11 and the start-a-task ritual now cover querying
  and refreshing the Graphify graph.
- README badge bumped to 1.2.0; INDEX gained an agent-memory reference row.

## [1.1.0] - 2026-11-26

### Added

- README and MIT license for open-source release.

### Changed

- Content fixes across the boot sequence, agent lifecycle protocol, role
  cards, testing strategy thresholds, and phase 07 task P07-T02.

## [1.0.0] - 2026-11-26

### Added

- Initial open-source release of the Engineering Manual: 11 SDLC phases,
  108 task cards, 12 agent roles, gates G0–G10, and the project ledger
  template.
