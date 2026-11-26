## 2.3 Standard classifications

**Data classification (default)**

| Class | Examples | Minimum controls |
|---|---|---|
| Public | Marketing content | Integrity controls |
| Internal | Internal docs, non-sensitive config | AuthN, access logging |
| Confidential | PII, business data, credentials metadata | AuthZ by need-to-know, encryption in transit and at rest, audit logging, masked in non-prod |
| Restricted | Secrets, authentication credentials, payment data, health data, government IDs | All Confidential controls, plus field-level or envelope encryption, a secrets manager or HSM/KMS, strict retention, and human approval for access |

**Vulnerability severity (default: CVSS base score adjusted by context)**

| Severity | Typical criteria | Mitigation target | Fix target |
|---|---|---|---|
| Critical | Remote unauthenticated compromise, mass data exposure, active exploitation | 24 h | 7 days |
| High | Authenticated privilege escalation, significant data exposure, BOLA/IDOR on sensitive data | 72 h | 30 days |
| Medium | Limited-impact flaws that need preconditions | n/a | 90 days |
| Low / Info | Hardening gaps, minor leaks | n/a | Backlog (review at 180 days) |

Exploitability evidence (for example CISA KEV listing or EPSS) MAY raise priority. Lowering severity needs a documented justification.

**Defect severity (functional):** S1 Blocker (core flow broken or data loss), S2 Major (important function impaired, no workaround), S3 Minor (workaround exists), S4 Cosmetic.
