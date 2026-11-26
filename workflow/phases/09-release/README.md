## PHASE 09 — PRODUCTION RELEASE AND DEPLOYMENT

**Purpose and why.** Releasing is the highest-risk routine activity. A disciplined, reversible release process with explicit approvals limits damage.

**Roles.** DevOps Engineer (executor), Orchestrator, Technical Reviewer, Security Engineer, QA Engineer, **Human Release Authority (mandatory approver)**.

### Tasks

| ID | Task | How to execute | Outputs | Validation |
|---|---|---|---|---|
| P09-T01 | **Pre-deployment verification** | Confirm that the artifact digest under test is the artifact to be deployed. Confirm G6, G7, and G8 are valid for this digest (not stale). Verify SBOM, signatures, and migration dry-run on a production-like snapshot. | Release candidate dossier | The digest match is recorded. |
| P09-T02 | **Release readiness assessment** | Walk the Release Readiness Checklist (§19.8): open defects, known issues, risk acceptances, capacity check, on-call coverage, comms plan, and a rollback plan with a tested time. | Readiness Report | All items green or waived by an authority. |
| P09-T03 | **Security approval** | The Security Authority reviews: the open finding list, exceptions with expiry, the secrets and config diff, and the new attack surface. | Security Approval record | Signed approval. |
| P09-T04 | **Production configuration and migration validation** | Verify config differences against the staging baseline (no debug flags, correct endpoints, and production-scope credentials present only in the secrets manager). Validate that the migration is backward-compatible (expand phase) and that its backup is verified. | Config diff report, migration validation | Reviewer confirms the diff. |
| P09-T05 | **Deployment execution (human-approved, NN-04)** | Announce the change window. Take a backup or snapshot. Execute through the pipeline with the chosen strategy (canary or blue/green by risk). Watch the dashboards at each step. The agent MUST NOT proceed past a failed health gate. | Deployment log | The pipeline log shows the approved run ID and approver. |
| P09-T06 | **Smoke tests and health checks** | Automated smoke suite on critical paths (login, core transaction, and a read of the key data), health endpoints (liveness and readiness), key metrics inside the SLO for N minutes, security headers and TLS check, and a synthetic monitor check. | Smoke report | All pass. Otherwise execute P09-T07. |
| P09-T07 | **Rollback decision (if triggered)** | Triggers: failed smoke test, SLO breach, a security regression, or data integrity anomalies. Execute the rollback runbook (traffic shift back, previous artifact, compatible schema). Record the incident. | Rollback record | Verified restore of the prior state, plus a post-rollback smoke test. |
| P09-T08 | **Release documentation and change management** | Release notes (user-facing and internal), the change record (what, why, who approved, the rollback), a version tag, and RTM updates (requirement → release). Deployment Report. | Release notes, Deployment Report | G9 and G10 recorded. |

**Security controls.** Production access is just-in-time and logged. The two-person rule for irreversible actions. Freeze windows are respected. Feature flags default to off for risky features. Post-deploy, rotate any credentials that were used in the change.

**Deliverable.** Verified production release and deployment report. **Failure handling.** See P09-T07. **Transition.** G10 → P10 (hypercare: heightened monitoring for a defined period, such as 24–72 h).

---
