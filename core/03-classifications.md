## 2.3 Standard classifications

**Data classification (default)**

| Class | Examples | Minimum controls |
|---|---|---|
| Public | Marketing content, public docs | Integrity controls |
| Internal | Internal docs, non-sensitive config, code structure | AuthN, access logging |
| Confidential | PII, business data, credentials metadata, sensitive architecture | AuthZ by need-to-know, encryption in transit and at rest, audit logging, masked in non-prod |
| Restricted | Secrets, authentication credentials, payment data, health data, government IDs, exploit details | All Confidential controls, plus field-level or envelope encryption, secrets manager or HSM/KMS, strict retention, human approval for access, restricted storage |

**Data handling by class**

| Class | Non-production use | External model/tool egress | Logging/evidence | Retention |
|---|---|---|---|---|
| Public | Allowed | Allowed on approved endpoints | Normal | Project policy |
| Internal | Allowed with access control | Approved endpoint; record data flow | Normal; avoid unnecessary detail | Project policy |
| Confidential | Anonymized/masked or Data Owner approval | Data Owner + Security Authority approval; approved contracted endpoint | Minimized; restricted if sensitive | Defined per data type |
| Restricted | Prohibited unless explicitly approved and isolated | Data Owner + Security Authority approval; minimize/mask/tokenize; secrets never sent | Restricted storage with access logging | Strictest applicable; delete when no longer needed |

Lowering a classification or handling rule requires a documented decision by
the Data Owner and, for Restricted data, the Security Authority.

**Vulnerability severity (default: CVSS base score adjusted by context)**

| Severity | Typical criteria | Mitigation target | Fix target |
|---|---|---|---|
| Critical | Remote unauthenticated compromise, mass data exposure, active exploitation | 24 h | 7 days |
| High | Authenticated privilege escalation, significant data exposure, BOLA/IDOR on sensitive data | 72 h | 30 days |
| Medium | Limited-impact flaws that need preconditions | n/a | 90 days |
| Low / Info | Hardening gaps, minor leaks | n/a | Backlog (review at 180 days) |

Exploitability evidence (for example CISA KEV listing or EPSS) MAY raise
priority. Lowering severity needs a documented justification. For agentic
systems, add business-impact context: autonomy, privilege, data access, and
blast radius can raise severity even when CVSS is moderate.

**Defect severity (functional):** S1 Blocker (core flow broken or data loss),
S2 Major (important function impaired, no workaround), S3 Minor (workaround
exists), S4 Cosmetic.

**Incident severity:** Sev1 (active exploitation, data breach, production
outage, or secret exposure), Sev2 (significant degradation or credible threat),
Sev3 (limited impact), Sev4 (informational). Severity drives response SLA and
notification requirements; humans decide external notification.
