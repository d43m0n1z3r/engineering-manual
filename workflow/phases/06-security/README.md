## PHASE 06 — CYBERSECURITY ENGINEERING AND SECURITY VALIDATION

**Purpose and why.** To verify, with evidence, that security requirements are met and that real-world attack paths have been tested and mitigated. It combines *engineering* (building security in), *offensive validation* (finding what we missed), and *defensive operations* (detecting and responding).

**Roles.** Security Engineer (lead), Penetration Tester (authorized scope only), DevOps Engineer, Technical Reviewer, and the Human Security Authority (approvals).
**Skills.** Cats 11, 14–20.

**Security controls (Phase 06 operations)** Tool credentials are scoped and short-lived. Scanners run only from approved hosts against allowlisted targets. Evidence is encrypted at rest. Findings with exploit details are access-restricted (need-to-know). No exploit code or details are placed in public tickets.

**Validation and acceptance.** 0 open Critical or High findings (or signed risk acceptance by the Security Authority with a compensating control and an expiry date). Every Medium has an owner and a due date. 100% of in-scope ASVS controls are assessed. Retest evidence exists for every closed finding. Detection tests prove alerts fire. The scan tools have been verified as functioning (seeded test).
**Deliverables.** Security Assessment Report, Vulnerability Register, Remediation Plan, Security Validation Evidence.
**Failure handling.** Out-of-scope discovery means stop, document, and notify. Tool errors or incomplete scans must be reported as "not covered" and never reported as "clean". A discovered live compromise or real data exposure triggers the IR plan immediately and notification of humans.
**Transition.** G7 → P08 and P09. Findings feed back to P03–P05.

---
