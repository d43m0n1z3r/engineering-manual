## 13.5 Infrastructure and edge standards
- TLS 1.2 minimum (1.3 preferred), automated certificate renewal with expiry alerts, and HSTS after verification.
- Default-deny network policy. The databases are not publicly reachable. The administrative interfaces are reachable only through the VPN or a zero-trust proxy with MFA.
- Egress controls for the workloads that process the untrusted URLs (SSRF mitigation).
- Immutable infrastructure preferred: replace rather than patch in place.
- Logs and metrics are shipped off-host. The audit logs are tamper-resistant and retained per the policy.

---
