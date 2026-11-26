### A. Security Engineering

| ID | Task | How to execute | Outputs | Validation |
|---|---|---|---|---|
| P06-T01 | Security requirements and architecture review (continuous) | At each increment: re-check REQ-S coverage, review design changes against the threat model, update the threat model for new trust boundaries, and review security-relevant ADRs. | Updated threat model, review notes | No design change without a threat-model delta check. |
| P06-T02 | Automated security controls in CI (SAST, SCA, secrets, IaC, container) | Configure the tools with baselines, severity thresholds, and fail rules. Tune false positives only with a documented justification and reviewer approval. Track findings in the Vulnerability Register. | Pipeline security stages, baseline | Intentional seeded-vulnerability test proves the tools detect a known issue (verifies the tool works). |
| P06-T03 | Security control implementation verification | For each REQ-S control, produce a test or review that shows it works (not merely that it exists). | Control verification matrix | 100% of REQ-S verified or have an accepted risk. |
