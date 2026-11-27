# Requirements Traceability Matrix

| Requirement | Story | Design | Control | Code/PR | Test | Evidence | Vulnerability | Release |
|---|---|---|---|---|---|---|---|---|

## Conventions

- Requirement IDs: `REQ-F-###`, `REQ-N-###`, `REQ-S-###`, `REQ-P-###`.
- Every row should resolve to artifacts; use `N/A` only with justification.
- Security requirements must name the control and the test that verifies it.
- Orphans to check: requirements without tests, tests without requirements,
  code without requirements, vulnerabilities without requirements/fixes.

## Review cadence

- Check at G1 (requirements/design), G6/G7 (testing/security), and G9 (release).
- The Technical Reviewer records orphan findings as defects or CCRs.
