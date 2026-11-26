## 14.2 Incident severity and the response

| Severity | Definition | Response target | Required actions |
|---|---|---|---|
| Sev1 | A major outage, a confirmed breach, or the data exposure | Immediate. The incident commander is assigned. | A human lead, containment first, evidence preservation, the legal and privacy notification assessment (by humans), and updates at a fixed cadence |
| Sev2 | The significant degradation, or the suspected compromise | ≤ 30 min | The responder engaged, the investigation, and the mitigation |
| Sev3 | A minor impact, with a workaround | Business hours | Track and fix |
| Sev4 | The cosmetic or informational | Backlog | Track |

**Incident procedure.** (1) Detect and triage. (2) Declare the severity and assign the roles. (3) Preserve the evidence (the logs, the snapshots) before the remediation where practical. (4) Contain (revoke the credentials and the tokens, isolate, block, and the feature-flag off). (5) Eradicate (remove the root cause, patch). (6) Recover (restore from the verified-clean state and monitor). (7) Blameless post-incident review with the tracked actions. (8) Update the detections, the runbooks, the threat model, and the tests.

For suspected compromise, **rotate** the potentially exposed secrets and keys, and treat the exposed data per the privacy obligations flagged to the humans.
