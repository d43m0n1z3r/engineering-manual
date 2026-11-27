## 11.5 Security validation methods (mapping)

| Control or risk | Verification |
|---|---|
| Injection | SAST rules, negative tests, DAST, and the code review |
| Access control | The authZ matrix tests with multi-identity, the manual BOLA and BFLA testing |
| Authentication | The brute-force and lockout tests, the token tamper tests, the session lifecycle tests, and the reset flow review |
| Cryptography | The code review against the crypto checklist, the TLS scan, and the key rotation drill |
| Secrets | The secret scans (the working tree, the history, the images), and the config review |
| Configuration | The CIS scans, the header and the TLS checks, and the IaC scans |
| Supply chain | The SBOM review, the signature verification negative test, dependency review, and CI provenance checks |
| Logging and detection | The simulated events fire the alerts, and the log review shows no sensitive data |
| Resilience to abuse | The rate-limit tests and the resource exhaustion tests (non-production, within the scope) |
| Prompt/content injection | Seeded-instruction tests, untrusted-content handling review, blocked-action logs |
| Tool poisoning / MCP | Tool metadata/output poisoning tests, rug-pull change detection, schema validation |
| Agentic supply chain | Tooling Register review, pinning/digest checks, vetting checklist evidence |
| Data egress | Egress allowlist review, classification checks, approval records for Confidential/Restricted flows |
| Confused deputy / excessive agency | Deny-by-default authZ tests, scoped credential review, approval binding checks |
