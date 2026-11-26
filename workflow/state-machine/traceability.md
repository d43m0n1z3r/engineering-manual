## 9.3 Traceability chain (must be unbroken)

`REQ-ID → Story/Use case → Design element (component, API, table) → Control (for REQ-S) → Code (commit/PR) → Test case (TC-ID) → Test result evidence → Vulnerability (VULN-ID, if any) → Release (version tag)`

The Technical Reviewer checks for **orphans** (requirements without tests, tests without requirements, and code without a requirement) at G1, G6, and G9.

---
