# Contributing

This repository is the living Engineering Manual. Contributions change the
process that agents and humans follow, so treat normative edits as governed
changes, not casual docs edits.

## Before you start

1. Read [`AGENTS.md`](AGENTS.md), [`INDEX.md`](INDEX.md), and
   [`REPORT.md`](REPORT.md) (known limitations and provenance).
2. For process, threshold, gate, evidence, or security-control changes, follow
   [`AMENDMENT-PROCESS.md`](AMENDMENT-PROCESS.md).
3. Keep `source/manual.md` frozen; it is the audit baseline, not a live mirror.

## Repository checks

Run before opening a pull request:

```bash
python3 scripts/build_task_registry.py --check
python3 scripts/check_manual.py
```

If you change phase task tables, regenerate `workflow/task-registry.json` with
`python3 scripts/build_task_registry.py`. If you change the role catalogue,
update the derived role cards in the same change. Task and role cards are
derived convenience views; keep them consistent with their source tables.

## Change expectations

- Link related files instead of duplicating rules; keep `INDEX.md`, `XREF.md`,
  and `TASKS.md` accurate when structure changes.
- Do not commit secrets, credentials, Restricted data, or exploit details.
- Add a `CHANGELOG.md` entry under `[Unreleased]` for user-visible changes.
- Security-sensitive paths (`core/`, `workflow/gates/`,
  `workflow/phases/06-security/`, `agents/`, `scripts/`, `.github/`) require the
  reviewers listed in [`CODEOWNERS`](CODEOWNERS).
