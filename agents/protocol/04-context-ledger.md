## 8.5 Context preservation (project ledger)

Agents have limited memory and no guarantee of continuity. Therefore **the repository is the memory**. The ledger lives in version control:

| File or folder | Purpose | Updated by |
|---|---|---|
| `STATE.md` | Current phase, active tasks, the gate status, blockers, and the next actions | Orchestrator, and every agent on state changes |
| `ASSUMPTIONS.md` | Assumptions: ID, statement, owner, impact, validation, status | All |
| `DECISIONS/ADR-###.md` | The architectural and technical decisions | Architect and others |
| `EVIDENCE/EVD-###` | The evidence records (§2.4) | Task executor |
| `RTM.md` (or tool) | Traceability: REQ → design → code → test → release | All, checked by the Reviewer |
| `RISKS.md` | The risk register | Analyst, Security |
| `VULNS.md` (restricted access) | The Vulnerability Register | Security |
| `LOG/` | Execution logs (§8.12) | Every agent |
| `HANDOFFS/` | Handoff packets | Every agent |
| `GLOSSARY.md` | The ubiquitous language and the terms | All |

**Start-of-task ritual** (mandatory): (1) Read `STATE.md`, the task definition, and the linked ADRs and handoffs. (2) Restate the objective and the preconditions in the log. (3) Verify the preconditions with evidence. (4) Identify missing information. (5) Claim the task. **End-of-task ritual:** (1) Submit outputs and evidence. (2) Update `STATE.md`, `RTM.md`, and the docs. (3) Write the handoff. (4) Log the lessons and the open issues.

## 8.6 Documentation updates
Any change to behavior, interface, configuration, infrastructure, or security posture MUST update the affected documents **in the same change set**. The Reviewer rejects a change that has stale docs (the "docs-with-code" rule).
