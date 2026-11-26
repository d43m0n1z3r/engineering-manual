# PART 11 — TESTING AND VALIDATION STANDARDS

## 11.1 Test strategy (pyramid and the supplements)

| Level | Share of the effort (guidance) | Speed | Scope |
|---|---|---|---|
| Unit | Majority | ms | Functions, classes, and the domain rules |
| Component | Moderate | Seconds | UI components in isolation. Service modules |
| Integration and API | Moderate | Seconds | Real DB or broker, authZ, and serialization |
| Contract | As the boundaries require | Seconds | Consumer and provider agreement |
| End-to-end | Minimal, critical journeys | Minutes | Whole system |
| Non-functional | Scheduled and pre-release | Minutes to hours | Performance, reliability, and accessibility |
| Security | Continuous | Varies | Automated regression plus the scoped manual testing |

## 11.2 Quantitative standards (defaults)

| Metric | Threshold | Notes |
|---|---|---|
| Line and branch coverage (overall) | ≥ 80% line, ≥ 70% branch | Coverage is a floor, not a goal. Reviewers check the assertion quality. |
| Coverage on security-critical modules (authN, authZ, crypto, validation, payments) | ≥ 90% branch | Plus the negative tests. |
| Mutation score on critical modules (where tooling supports it) | ≥ 70% | Recommended. For security-critical modules (validation, authentication, authorization, parsing), mutation testing SHOULD be run, and surviving mutants are logged as findings until killed or justified. |
| Critical-path E2E pass rate | 100% | |
| Flaky-test rate | < 2% of the runs | Quarantine policy applies. |
| Unit suite duration | < 5 min on CI (guidance) | |
| API contract conformance | 100% | |
| AuthZ matrix coverage | 100% of endpoints × roles | |
| Accessibility | 0 critical and 0 serious automated violations. WCAG 2.2 AA manual checks on the key flows | |
| Performance | Meets the NFR (for example p95 latency at the target load, error rate < 0.1%). No regression > 10% against the baseline without a justification | |
| Load test | The expected peak sustained for ≥ 30 min. Stress to the point of the failure, documented. Soak ≥ 4 h for the leak detection (adjust by the system) | |
| Static analysis | 0 High or Critical open. Complexity limit per function (for example cyclomatic ≤ 10, with the exceptions justified) | |
| Dependencies | 0 known-exploited vulnerabilities. High and Critical per the SLA | |
