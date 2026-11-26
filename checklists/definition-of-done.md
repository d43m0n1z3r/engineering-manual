# PART 18 — DEFINITION OF DONE (DoD)

## 18.1 Task-level DoD (all must be true)
- [ ] All the outputs in `expected_outputs` exist at the stated locations.
- [ ] All the `validation_criteria` pass, with the **evidence records** attached (current, non-stale).
- [ ] An independent reviewer has verified the work (the state is `VERIFIED`).
- [ ] The documentation and the RTM are updated in the same change.
- [ ] No secrets in the outputs, the logs, or the history (scan evidence).
- [ ] The handoff packet is written, and the receiver has acknowledged it.
- [ ] The assumptions, the known issues, and the debt are logged with IDs.
- [ ] `STATE.md` is updated.

## 18.2 Code-change DoD
- [ ] Acceptance criteria pass (positive, negative, abuse). [ ] Unit and integration tests are added or updated, and the coverage thresholds are met. [ ] SAST, SCA, and the secret scan show 0 new High or Critical. [ ] The input validation, the output encoding, the authZ, and the error handling are verified. [ ] The logging does not leak the sensitive data. [ ] The contract and the docs are updated. [ ] The migration is backward-compatible. [ ] The independent review is approved (G5). [ ] The CI is green.

## 18.3 Feature (story) DoD
- 18.2, plus: [ ] The acceptance criteria are demonstrated end to end. [ ] Accessibility checks pass (for the UI). [ ] The performance impact is measured against the budget. [ ] The telemetry (metrics, logs, traces, audit events) exists. [ ] The threat model delta is reviewed. [ ] The feature flag and the rollback are defined where applicable.

## 18.4 Phase DoD
- All the phase tasks are `DONE`. The phase deliverables are produced and reviewed. The phase's gate is approved by the authority with the recorded decision. The RTM has no orphans for the phase. The risks and the assumptions are updated.

## 18.5 Release DoD
- G6, G7, G8, and G9 are valid for the same digest. The release notes and the change record exist. The smoke and the SLO checks pass (G10). The rollback was verified as available. The monitoring and the alerts are active. The release tag is recorded in the RTM.

## 18.6 Project DoD (for the handover to operations)
- The documentation set (Part 12) is complete and executable by a new agent. The DR drill was done. The IR plan was exercised. The ownership, the on-call, and the maintenance plan are in place. The Improvement Roadmap is approved.

---
