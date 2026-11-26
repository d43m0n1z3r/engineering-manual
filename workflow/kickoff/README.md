## 3.2 Pre-phase: X-KICKOFF (G0)

| ID | Task | Execution | Output | Validation |
|---|---|---|---|---|
| X-KICKOFF-T01 | Establish project charter and authority | Record sponsor, product owner, Engineering Authority, Security Authority, and data owner. Define communication channels and approval authorities. | Charter, Authority Register | Humans have signed. Every gate has a named approver. |
| X-KICKOFF-T02 | Establish authorized environments and access | Create the access list: environments, repositories, tools, agent permission tiers (§7.3). Issue scoped credentials via a secrets manager. | Access Register | No shared or long-lived credentials. Reviewed by Security. |
| X-KICKOFF-T03 | Initialize project ledger | Create the repository folder structure for ledger files (§8.5): `STATE.md`, `ASSUMPTIONS.md`, `DECISIONS/`, `EVIDENCE/`, `RTM.md`, `RISKS.md`, `MEMORY.md`. If the project uses Graphify, build or update `graphify-out/` and confirm agents can query it. | Ledger | Files exist and are version controlled; `graphify-out/` exists and is current when Graphify is configured. |
| X-KICKOFF-T04 | Establish test and offensive-security authorization baseline | Record which environments exist and who may authorize security testing. Default is no active testing until an RoE exists. | Authorization Baseline | Security Authority signature. |

---
