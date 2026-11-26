# Changelog

All notable changes to the Engineering Manual are documented here. The
`engineering-manual/` directory is the living repository — changes land there
continuously under `[Unreleased]`. A version number is bumped and a dated
section is added only when a release is cut; versioned snapshots live in
sibling directories (`engineering-manual-X.Y.Z/`).

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

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

## [1.1.0]

### Added

- README and MIT license for open-source release.

### Changed

- Content fixes across the boot sequence, agent lifecycle protocol, role
  cards, testing strategy thresholds, and phase 07 task P07-T02.

## [1.0.0]

### Added

- Initial open-source release of the Engineering Manual: 11 SDLC phases,
  108 task cards, 12 agent roles, gates G0–G10, and the project ledger
  template.
