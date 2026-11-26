# Repository scripts

Stdlib-only Python 3 helpers for keeping the manual consistent.

- `build_task_registry.py` regenerates [`workflow/task-registry.json`](../workflow/task-registry.json)
  from the task cards plus curated orchestration metadata. Run
  `python3 scripts/build_task_registry.py`; CI uses `--check` to fail when the
  registry is stale.
- `check_manual.py` verifies the manifest, generated-artifact counts, relative
  links, task cards and task-table consistency, `§` references through `XREF.md`,
  registry schema/references/cycles, checklist run-on items, and obvious secret
  patterns. Run `python3 scripts/check_manual.py`.

## Derived artifacts

Task cards are derived from the phase task tables, role cards from
`agents/roles/README.md`, and `XREF.md`/`manifest.json` from `source/manual.md`.
The original generator is not in this repository; when changing phase tables or
the role catalogue, update the derived cards in the same change and run the
checks above. `workflow/task-registry.json` is the only derived artifact with an
in-repository generator.
