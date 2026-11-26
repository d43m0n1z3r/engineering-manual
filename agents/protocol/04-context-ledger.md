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
| `graphify-out/` (Graphify knowledge graph) | Queryable memory of the codebase, docs, and decisions for agents | Every agent, when Graphify is configured |

**Agent memory (Graphify).** When the project uses
[Graphify](https://github.com/Graphify-Labs/graphify) — the `/graphify` skill
that turns the repository into a queryable knowledge graph — it complements,
never replaces, the ledger. Before starting work, agents MUST query the graph
(`graphify query`/`path`/`explain`, the `--wiki` index, or the MCP server)
for facts tied to the affected files, symbols, and domain. After every
addition, change, or fix, agents MUST refresh the graph (`graphify . --update`,
or the configured `--watch` / post-commit hook) in the same change set as the
ledger update, so agent memory never goes stale.

**Start-of-task ritual** (mandatory): (1) Read `STATE.md`, the task definition, and the linked ADRs and handoffs. (1a) When Graphify is configured, query the graph for facts tied to the task's files, symbols, and domain. (2) Restate the objective and the preconditions in the log. (3) Verify the preconditions with evidence. (4) Identify missing information. (5) Claim the task. **End-of-task ritual:** (1) Submit outputs and evidence. (2) Update `STATE.md`, `RTM.md`, and the docs. (2a) Refresh the Graphify graph (`--update`, or the configured watch/hook) so it reflects this task's changes. (3) Write the handoff. (4) Log the lessons and the open issues.

## 8.6 Documentation updates
Any change to behavior, interface, configuration, infrastructure, or security posture MUST update the affected documents **in the same change set**. The Reviewer rejects a change that has stale docs (the "docs-with-code" rule).
