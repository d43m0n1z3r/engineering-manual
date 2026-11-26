## 2.2 Engineering principles made operational

| Principle | Operational rule (what the agent does) | How it is verified |
|---|---|---|
| Security by Design | Threat model precedes implementation. Every REQ-S has a design control and a test. | Gate G3 and G4 evidence. Traceability matrix has no empty security rows. |
| Secure by Default | Defaults are deny, closed, encrypted, and least-privileged. Debug is off, CORS is closed, cookies are `Secure`, and new endpoints require authN and authZ. | Config review. Automated default-config tests. |
| Defense in Depth | Every critical asset is protected by at least two independent controls. Example for SQLi: parameterized queries, DB least privilege, and WAF/monitoring. | Control mapping table in the Security Architecture. |
| Least Privilege / Zero Trust | Service accounts have scoped roles. Internal calls are authenticated. No implicit trust by network location. | IAM policy review. Negative authZ tests. |
| Separation of Concerns | Presentation, application logic, domain, and persistence are distinct. Cross-layer imports are enforced by tooling. | Architecture fitness tests (for example dependency-rule checks). |
| SOLID | SRP (one reason to change per module). OCP (extend through interfaces). LSP (substitutable implementations). ISP (small interfaces). DIP (depend on abstractions at boundaries). | Code review checklist (§19.3). Static analysis for coupling and complexity. |
| DRY, KISS, YAGNI | Deduplicate *knowledge*, not coincidental similarity. Choose the simplest design that meets measured requirements. Do not build features or scale paths without a requirement. | Reviewer challenges any abstraction without a second use case. ADR "simpler alternative considered". |
| Modular, loosely coupled | Modules interact through versioned contracts. No shared mutable database tables across module boundaries. | Contract tests. Dependency graph review. |
| Reliability and fault tolerance | Timeouts, retries with jittered backoff, idempotency, circuit breakers, and graceful degradation where dependencies fail. | Fault-injection and resilience tests (§11.4). |
| Scalability and performance | Targets come from NFRs. Measure first, then optimize. | Baselines and load test reports. Profiling evidence. |
| Maintainability and extensibility | Cyclomatic complexity and module size are bounded. Documentation is current. | Static metrics gates. Docs-as-code checks. |
| Automation and reproducibility | Builds, tests, infrastructure, and deployments are scripted and deterministic. No manual snowflake changes. | Clean-room rebuild test. Drift detection. |
| Observability and accountability | Structured logs, metrics, traces, and audit logs with correlation IDs. Every privileged action is attributable. | Log schema tests. Audit trail sampling. |
| Continuous improvement | Retrospectives and metrics feed the roadmap. | Phase 11 deliverables. |
