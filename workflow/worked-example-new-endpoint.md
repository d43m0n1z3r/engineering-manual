# APPENDIX B — WORKED EXAMPLE: "ADD A NEW ENDPOINT" ACROSS THE WORKFLOW

| Step | Agent | Action | Evidence produced |
|---|---|---|---|
| 1 | Project Analyst | Adds REQ-F-042 ("Users can download their own invoices") and REQ-S-017 ("Users MUST only access invoices they own"), plus an abuse case ("A user guesses another invoice ID") | Updated spec, RTM row |
| 2 | Architect and Security Engineer | A threat-model delta: THR-031 (BOLA on invoice ID). A control: the ownership check in the policy layer, with opaque IDs. A contract change: `GET /invoices/{id}` | THR-031, the OpenAPI diff, ADR if needed |
| 3 | Backend Developer | Implements the endpoint. The authZ check is in the central policy layer. Writes the tests: owner OK, other user 404/403, the unauthenticated 401, the cross-tenant denied | PR, test report, SAST, and secret scan results |
| 4 | Technical Reviewer and Security Engineer | Independent review (G5), including a check of the authZ logic and that the logs have no PII | Review record |
| 5 | QA Engineer | The authZ matrix updated at 100%. A regression test is added. The rate-limit test | Test report |
| 6 | Penetration Tester (the RoE exists) | Tries the BOLA with 2 synthetic identities in staging | Test log, finding or the clean statement *with the limitations* |
| 7 | DevOps Engineer | The pipeline builds, signs, and deploys to staging. The release flows through G6, G7, G8, and then the human G9 | Pipeline evidence, the approvals |
| 8 | DevOps and Security (operations) | The new endpoint appears in the dashboards. The detection for anomalous invoice-access volume is tested | Alert test evidence |

---
