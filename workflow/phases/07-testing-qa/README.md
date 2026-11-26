## PHASE 07 — SOFTWARE TESTING AND QUALITY ASSURANCE

**Purpose and why.** Tests are executable specifications and the safety net that makes change safe. Quality gates make "done" measurable.

**Roles.** QA Engineer (lead), all developers (unit and component tests), Security Engineer, DevOps Engineer.
**Skills.** Cats 21, 22, 4.

### Tasks

| ID | Task | How to execute | Outputs | Validation |
|---|---|---|---|---|
| P07-T01 | **Test strategy and plan** | Define the test levels, the risk-based priorities (from the threat model and the risk register), environments, data strategy (synthetic data), entry and exit criteria, and tools. Map the test types to the requirements (RTM). | Test Plan | Every REQ has ≥ 1 TC. Every High risk has targeted tests. |
| P07-T02 | **Unit and component tests** | Test behavior, not implementation. Isolate with fakes or mocks at boundaries only. Boundary tests MUST use literal values taken from the requirement, not constants imported from the code under test. Cover edge cases, errors, and invariants. Use property-based testing for parsers and calculations. Tests are deterministic and fast. | Unit suites | Coverage thresholds (Part 11). Mutation testing on critical modules where feasible. |
| P07-T03 | **Integration, API, and contract tests** | Real database and message broker in containers (ephemeral). Test the repositories, migrations, authZ, and the serialization. Consumer-driven contract tests for service boundaries. Verify the error model and the status codes. | Integration suites | Contract conformance is 100%. |
| P07-T04 | **End-to-end and acceptance tests** | Cover critical user journeys only (testing pyramid). Stable selectors, explicit waits on conditions, isolated test data, and no inter-test dependencies. Run UAT with stakeholders against acceptance criteria. | E2E suite, UAT sign-off | Critical journeys pass on the supported browser matrix. |
| P07-T05 | **Non-functional tests: performance, load, stress, soak, reliability** | Establish baselines. Model realistic workloads from the NFRs. Load (expected peak), stress (beyond peak to find the breaking point and the degradation behavior), spike, and soak (memory leaks, resource exhaustion). Reliability: fault injection (dependency down, latency, packet loss, and DB failover), restart and recovery tests. | Perf and reliability reports | NFR thresholds met. Failure behavior matches the design (graceful degradation). |
| P07-T06 | **Compatibility and accessibility tests** | Browser and device matrix. Accessibility: automated (axe or equivalent), keyboard-only, and screen-reader checks. | Compat and a11y reports | 0 critical or serious a11y issues. |
| P07-T07 | **Security tests (with P06)** | Automated authZ matrix, negative input tests, CSRF and CSP checks, rate-limit checks, and header checks as regression tests. | Security regression suite | Every fixed vulnerability has a regression test. |
| P07-T08 | **Regression management, coverage analysis, defect tracking** | Run the full regression on every release candidate. Triage flaky tests (quarantine with an owner and a due date, since flakiness is a defect). Analyze coverage by risk, not only by percentage. Track defects (severity, steps, evidence, status, and linked requirement). | Coverage report, Defect Register | No S1 or S2 open. Flaky rate under the threshold. |
| P07-T09 | **Test report and G6 submission** | Summarize results with evidence per Part 2.4. State limitations honestly. | Test Report | Satisfies G6 criteria. |

**Validation and acceptance.** See Part 11 for thresholds. **Deliverables.** Test Plan, Automated Test Suites, Test Reports, Defect Register.
**Failure handling.** A failing test blocks merging, and tests are never disabled to pass. A flaky test is quarantined with an owner and a deadline, then fixed or removed with a justification. A performance miss triggers profiling, then optimization or an NFR renegotiation through the Product Owner.
**Transition.** G6 → P09 (together with G7 and G8).

---
