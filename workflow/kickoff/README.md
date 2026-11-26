## 3.2 Pre-phase: X-KICKOFF (G0)

| ID | Task | Execution | Output | Validation |
|---|---|---|---|---|
| X-KICKOFF-T01 | Establish project charter and authority | Record sponsor, product owner, Engineering Authority, Security Authority, and data owner. Define communication channels and approval authorities. Record the process profile (for example exploratory, internal, production, or regulated) and any pre-approved tailoring; evidence, authorization, and ★ security criteria are never waived by profile. | Charter, Authority Register, Process Profile | Humans have signed. Every gate has a named approver. The process profile is recorded and deviations require an approved ADR. |
| X-KICKOFF-T02 | Establish authorized environments and access | Create the access list: environments, repositories, tools, agent permission tiers (§7.3). Issue scoped credentials via a secrets manager. | Access Register | No shared or long-lived credentials. Reviewed by Security. |
| X-KICKOFF-T03 | Initialize project ledger | Copy `ledger-template/` into the project repository or approved workspace. Confirm `STATE.md`, `ASSUMPTIONS.md`, `GLOSSARY.md`, `RTM.md`, `RISKS.md`, `MEMORY.md`, `DEFECTS.md`, `INCIDENTS.md`, `DECISIONS/`, `EVIDENCE/`, `HANDOFFS/`, `LOG/`, and `RESTRICTED/` exist; keep `RESTRICTED/VULNS.md` in approved restricted storage. If the project uses Graphify, build or update `graphify-out/` and confirm agents can query it. | Ledger | Files exist and are version controlled; `RESTRICTED/VULNS.md` is access-restricted; `graphify-out/` exists and is current when Graphify is configured. |
| X-KICKOFF-T04 | Establish test and offensive-security authorization baseline | Record which environments exist and who may authorize security testing. Default is no active testing until an RoE exists. | Authorization Baseline | Security Authority signature. |

---
