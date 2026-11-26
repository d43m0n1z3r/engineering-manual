# Manual Amendment Process

Normative changes to this manual change how agents and humans work. They MUST
follow this process rather than landing as unreviewed edits.

## What requires amendment review

- Non-negotiables, evidence standards, data classifications, and status language.
- Gates G0–G10, the gate-bypass policy, and ★ criteria.
- Task schemas, lifecycle/state rules, dependencies, and approval matrices.
- Security controls, RoE requirements, permission tiers, and prohibited actions.
- Numeric thresholds (coverage, SLOs, SLAs, retention, hypercare windows).

Typo, link, formatting, and navigation fixes may use the normal contribution
flow but still require `scripts/check_manual.py` to pass.

## Approval

| Change area | Approving authority |
|---|---|
| Requirements scope and product process | Product Owner |
| Engineering process, thresholds, task/gate mechanics | Engineering Authority |
| Security controls, ★ criteria, RoE, classifications, agent-threat rules | Security Authority |
| Release and operations gates | Release/Operations Authority |

For this repository, maintainers act as the authorities until a project assigns
named humans. Agent-authored amendments are proposals, never self-approved.

## Required evidence for an amendment

1. Problem statement and impacted sections/tasks/gates.
2. At least one alternative considered and why it was rejected.
3. For threshold changes: the data, incident, or metric justifying the value.
4. For security-relevant changes: a short threat/risk note.
5. Updated derived artifacts (task/role cards, `workflow/task-registry.json`,
   `XREF.md`, `INDEX.md`, `TASKS.md` as applicable).
6. `python3 scripts/build_task_registry.py --check` and
   `python3 scripts/check_manual.py` passing.
7. A `CHANGELOG.md` entry under `[Unreleased]`.

## Versioning and deprecation

- The repository is a living manual: changes accumulate under `[Unreleased]`.
- Cut a release only by bumping `manifest.json` `manual_version`, adding a dated
  `CHANGELOG.md` section, and tagging the snapshot; versioned snapshots live in
  sibling directories.
- Use SemVer: MAJOR for incompatible process/gate changes, MINOR for additive or
  backward-compatible changes, PATCH for corrections.
- Deprecate by marking the item deprecated in `CHANGELOG.md` and in place, point
  to the replacement, and keep it for at least one minor release or until the
  replacement is referenced everywhere; remove only in a MAJOR release.
