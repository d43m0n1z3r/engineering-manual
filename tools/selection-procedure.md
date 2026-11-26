# PART 6 — TOOLS AND TECHNOLOGY REFERENCE

## 6.1 Principles of selection
1. Requirements drive technology, not the reverse ([P01-T06](../workflow/phases/01-discovery-requirements/tasks/P01-T06.md)).
2. Prefer **boring, mature** technology unless a measured need justifies otherwise.
3. Prefer technology the operating team can actually run, secure, and debug.
4. Verify the maintenance status, release cadence, security advisory history, and license from the authoritative sources at the time of the decision.
5. Record the decision in an ADR, including an exit strategy for lock-in.

## 6.2 Weighted decision matrix (standard procedure)

| Criterion | Default weight | What to check (evidence) |
|---|---|---|
| Security | 20% | Advisory history and response time, secure defaults, memory safety, and the auth ecosystem |
| Reliability | 12% | Production track record, failure-mode documentation |
| Scalability | 8% | Documented limits and measured benchmarks vs. NFR |
| Maintainability | 10% | The readability, the typing, the testability, and the upgrade path |
| Performance | 8% | Benchmarks relevant to the workload |
| Ecosystem maturity | 8% | Libraries, tooling, and the integrations |
| Documentation | 6% | Accuracy and completeness |
| Community and vendor support | 8% | Release cadence, contributors, bus factor, and the LTS |
| Operational complexity | 12% | Skills needed, moving parts, upgrade and backup effort |
| Cost efficiency | 8% | License, infrastructure, and staffing cost |

**Procedure.** (1) Adjust the weights with the stakeholders (the sum is 100%). (2) Score 1–5 per criterion using **evidence**, not impression. (3) Compute the weighted score. (4) Run a sensitivity check (does the winner change if the weights shift by ±5 points?). (5) Run a proof-of-concept on the top two if the scores are within about 10%. (6) Record the ADR. An unverified score MUST be marked "assumed".
