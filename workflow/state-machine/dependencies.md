## 9.2 Dependency table

| Task or phase | Hard dependencies | Gate required | Feeds |
|---|---|---|---|
| P01-T01..T08 | X-KICKOFF | G0 | P01-T09 |
| P01-T09 | P01-T01..T08 | | G1 |
| P02-T01..T08 | P01-T09 | G1 | P02-T09 |
| P02-T07 (threat model) | P02-T03, P02-T06 (DFD, controls) | G1 | G3 |
| P03-T04+ | P02-T09 | G2, G3, G4 | P03-T09 |
| P04-T01+ | P02-T09 | G2, G3, G4 | P04-T10 |
| P05-T03+ | P05-T02, P02-T09 | G2, G3, G4 | P05-T09 |
| P04-T04 (authZ) | P04-T02, P05-T02 | | P04-T05 |
| P06-T04 (RoE) | A deployable test environment (P08-T05) | G0 baseline plus the Security Authority | P06-T05 and later |
| P07-T05 (NFR tests) | A deployable staging environment | | G6 |
| P08-T11 | P08-T01..T10 | | G8 |
| P09-T01 | | G6, G7, G8 | P09-T05 |
| P09-T05 | P09-T01..T04 | G9 | P09-T06 |
| P10 | | G10 | P11 |
| P11 | Operational data | | New cycle |

## Machine-readable orchestration

`workflow/task-registry.json` is the authoritative machine-readable task graph
for scheduling. This table remains the human-readable dependency summary. Regenerate
the registry with `scripts/build_task_registry.py` after changing task cards or
curated orchestration metadata; run `scripts/task_readiness.py` to compute READY
tasks from verified dependencies and approved gates.
