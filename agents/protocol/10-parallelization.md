## 8.14 Parallelization rules

Parallel work is allowed only when dependencies, permissions, and shared state
allow it. The [task registry](../../workflow/task-registry.json) declares
`depends_on`; the Orchestrator enforces it.

| Can run in parallel | Condition |
|---|---|
| P03, P04, P05 | After G2, G3, and G4. API contract and data model frozen/versioned. Use mock servers. |
| P08 pipeline foundation with P03–P05 | After G2. Separate resource locks for environments and credentials. |
| P06 continuous activities (T01–T03, T11–T13) and P07 | Shift-left alongside development; no shared mutable target. |
| Multiple tasks within a phase | No data dependency and no shared write target. |
| Reviews of independent artifacts | Always, preferably by a different model/tool. |
| Test writing and implementation | Yes (test-first or paired). |

| Must be sequential | Reason |
|---|---|
| P01 → G1 → P02 | Architecture follows approved requirements. |
| P02-T07 threat model → affected implementation | Security by design. |
| RoE approval → offensive tasks | Authorization. |
| P06-T05 → T06 → T07 → T09 → T10 | Each step depends on the previous. |
| G6, G7, G8 → G9 → production deployment | Release safety. |
| DB migration expand → app deploy → contract later | Compatibility. |
| Vulnerability fix → retest → closure | Verification. |
| Shared ledger writes | Serialize or use per-task files merged by Orchestrator. |
| Shared environment/credential | Resource lock with owner, scope, expiry. |

Merge/serialization rule: when parallel branches touch the same file, contract,
migration, or config, the later change rebases, re-runs validation, and requests
re-review if semantics changed.
