# Project Ledger Template

Copy the contents of this directory into the project repository or another
approved, access-controlled project workspace.

Do not store credentials or sensitive production data in these files.
Use restricted storage for vulnerability details and sensitive evidence.

See the manual's agent protocol for lifecycle, evidence, and handoff rules.
`MEMORY.md` defines how agents query and refresh the Graphify knowledge graph
alongside the ledger.

## Register locations

- `STATE.md`, `ASSUMPTIONS.md`, `GLOSSARY.md`, `RTM.md`, `RISKS.md`,
  `DEFECTS.md`, `INCIDENTS.md`, `DECISIONS/`, `EVIDENCE/`, `HANDOFFS/`,
  `LOG/`, and `MEMORY.md` are the normal project ledger.
- `RESTRICTED/VULNS.md`, sensitive evidence, and restricted incident details
  belong in approved restricted storage; directory names do not enforce access
  control.
- Agent capability validation results belong in the Agent Capability Register
  (`/docs/agents` or the approved equivalent).
- `graphify-out/` is generated agent memory; follow the output policy in
  `MEMORY.md` (default: gitignored and regenerated, not committed).
