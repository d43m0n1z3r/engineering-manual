# Defect Register

| ID | Severity | REQ/TC | Steps to reproduce | Expected | Actual | Evidence | Owner | Status | Due |
|---|---|---|---|---|---|---|---|---|---|

ID format: `DEF-###`. Severity uses S1–S4 from `core/03-classifications.md`.

Status values: NEW, TRIAGED, IN_PROGRESS, FIXED, VERIFIED, CLOSED,
WONTFIX (justified), DUPLICATE.

Rules:

- Every defect links to requirement/test where possible; out-of-scope defects
  are still logged as findings with severity.
- FIXED requires a fix reference and retest evidence; VERIFIED requires
  independent or QA confirmation.
- Flaky defects are marked with reproduction rate and quarantine owner/deadline.
