### B. Offensive Security (authorized only)

**Authorization prerequisites (hard gate: P06-T04).**
No offensive step may begin until the **RoE document** is approved by the Security Authority and the system owner. It states:

| RoE field | Content |
|---|---|
| Scope | Explicit targets (hosts, URLs, APIs, IP ranges), environment (preferably isolated staging with synthetic data) |
| Out of scope | Third-party services, production unless separately approved, other tenants, personal data of real users, physical and social engineering unless authorized |
| Window | Dates, times, and contacts |
| Permitted techniques | Listed by category. Exploitation depth is limited (proof-of-concept without data exfiltration). |
| Prohibited | DoS or destructive tests, persistence beyond the session, data exfiltration or modification of real data, lateral movement outside scope, and credential reuse outside scope |
| Stop conditions | Unexpected impact, out-of-scope discovery, or data exposure leads to an immediate stop and notification |
| Data handling | Evidence is stored encrypted, secrets are redacted in reports, and retention is limited |
| Emergency contact | Named human |

| ID | Task | How to execute | Outputs | Validation |
|---|---|---|---|---|
| P06-T04 | **Authorization and RoE** | Draft the RoE (template in Part 17). Obtain the signature. Verify that target ownership is confirmed. Set up the isolated test environment. | Signed RoE | Human signature. Scope allowlist is configured in the tooling (tools technically restricted to in-scope targets). |
| P06-T05 | **Reconnaissance, asset discovery, enumeration** | Start with the project's own asset inventory and architecture. Use passive methods first. Active scanning only against in-scope targets at rate-limited settings. Enumerate endpoints (from OpenAPI, crawl, and routes), technologies, versions, and exposed services. Compare with the intended attack surface to find *shadow assets*. | Asset and endpoint inventory, discrepancy list | Every discovered asset is in scope or flagged and reported (not tested). |
| P06-T06 | **Vulnerability assessment** | Run scanners (network, web, container, dependency, IaC). Triage: confirm, de-duplicate, classify with CWE, score CVSS plus context, and mark false positives with evidence. | Candidate vulnerability list | Each finding has evidence, CWE, and reproduction steps, or is marked "unconfirmed". |
| P06-T07 | **Web, API, authentication, and authorization testing** | Follow OWASP WSTG and the ASVS at the chosen level, and the API Security Top 10: **AuthN** (credential policy, brute-force controls, MFA bypass, session fixation, token flaws, password reset flows). **AuthZ** (BOLA/IDOR, function-level access, privilege escalation, multi-tenant isolation, mass assignment, forced browsing). **Input handling** (injection classes, XSS, XXE, deserialization, SSRF, file upload, path traversal, open redirect). **Logic** (workflow bypass, race conditions, replay, coupon and price manipulation). **Config** (headers, CORS, TLS, verbose errors, default credentials, exposed admin and debug interfaces). **API** (rate limits, versioning, excessive data exposure, GraphQL depth and batching abuse). Use two or more test identities per role to test horizontal access. | Test log, findings | Each ASVS control in scope is marked pass, fail, or not applicable (with reasons). |
| P06-T08 | **Network, infrastructure, and configuration assessment** | Port and service review, TLS configuration, cloud IAM and exposure review (config review preferred over active attack), container and host benchmark checks (CIS), and secret exposure review. | Config assessment report | Benchmark deviations are documented with risk acceptance or remediation. |
| P06-T09 | **Controlled exploitation, privilege escalation, and post-exploitation impact assessment (where authorized)** | **Requires explicit human approval per finding class** (NN-04). Use the minimum proof needed (for example read a canary record, not real data). Do not establish persistence, do not exfiltrate real data, and do not damage the system. Document the attack chain and map it to MITRE ATT&CK. Assess blast radius analytically where further exploitation is not authorized. Stop at the first proof of impact. | Proof-of-concept evidence, impact analysis | Evidence shows reproducibility and the minimal-impact method. All artifacts are cleaned up and the system is restored. |
| P06-T10 | **Reporting and remediation verification** | Report: executive summary, scope and methodology, findings (title, severity, CWE, affected assets, description, reproduction steps, impact, evidence, remediation, references), positive observations, limitations (what was NOT tested). After fixes, **retest** each finding and record the result. | Security Assessment Report, Vulnerability Register, Remediation Plan | Every finding is Closed-Verified, Accepted-Risk (signed), or scheduled with an owner and date. |
