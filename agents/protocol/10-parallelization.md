## 8.14 Parallelization rules

| Can run in parallel | Condition |
|---|---|
| P03, P04, P05 | After G2, G3, and G4. The API contract and the data model are frozen (versioned). Use mock servers. |
| P08 (pipeline foundation) with P03–P05 | After G2. |
| P06 continuous activities (T01–T03, T11–T13) and P07 | Run alongside the development, as shift-left. |
| Multiple tasks within a phase | If there is no data dependency and no shared write target. |
| Reviews of independent artifacts | Always. |
| Test writing and implementation | Yes (test-first or paired). |

| Must be sequential | Reason |
|---|---|
| P01 → G1 → P02 | Architecture must follow approved requirements. |
| P02-T07 (threat model) → implementation of the affected components | Security by design. |
| RoE approval → any offensive task | Authorization. |
| P06-T05 (recon) → T06 → T07 → T09 → T10 | Each step depends on the previous. |
| G6, G7, G8 → G9 → production deployment | Release safety. |
| DB migration expand → app deploy → contract (later release) | Compatibility. |
| Vulnerability fix → retest → closure | Verification. |
