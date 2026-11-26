### E. Security tooling (categories; selection per Part 6)

| Category | Purpose | Tier |
|---|---|---|
| SAST | Find code-level flaws pre-merge | Essential |
| SCA and dependency scanning, SBOM | Known-vulnerable and license-problem dependencies | Essential |
| Secret detection (pre-commit and CI, history) | Prevent credential leaks | Essential |
| IaC scanning | Misconfigured cloud and infrastructure code | Essential for IaC projects |
| Container image scanning | OS and library CVEs in images | Essential for containerized projects |
| DAST | Runtime web and API flaws in staging | Recommended |
| Interactive or API fuzzing | Robustness and parsing flaws | Specialized |
| Vulnerability scanners (network and host) | Exposure and patch status | Recommended |
| Pentest proxy and manual tooling | Manual validation (authorized only) | Specialized |
| Network analysis | Traffic and TLS analysis in the lab and scope | Specialized |
| SIEM, log analytics, EDR, WAF | Detection and response | Recommended (scale-dependent) |
