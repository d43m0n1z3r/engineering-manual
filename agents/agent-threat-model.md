# Agent Ecosystem Threat Model and Controls

> Applies to AI agents, agent skills, MCP servers, plugins, hooks, tools, ledgers,
> model endpoints, and external model/tool providers. It complements NN-01..NN-10,
> the software threat model in Phase 02/06, and the agent operating model in
> [operating-model.md](operating-model.md).
>
> Reference points: OWASP Agentic AI Top 10, OWASP MCP Top 10, NIST AI RMF, and
> SLSA/in-toto for agent/tool supply chain. Verify current editions before use.

## Threat classes and required controls

| Threat class | Examples | Required control | Evidence |
|---|---|---|---|
| Prompt/content injection | Instructions embedded in repo files, issues, tool output, web pages, MCP responses, or user uploads | Treat external content as data (NN-07); stop and escalate on embedded instructions; keep untrusted content out of privileged prompts; use structured outputs and allowlists where possible | `LOG/` entry, review note, blocked-action record |
| Tool poisoning and rug pulls | Malicious or changed tool descriptions, schemas, parameters, or return values; tool changes after approval | Vet and pin tooling ([tooling-governance.md](tooling-governance.md)); treat tool metadata/output as untrusted; re-vet on change; suspend on suspicion | Tooling Register, ADR, change-detection alert |
| Agentic supply chain compromise | Malicious skill, plugin, MCP server, model, dataset, A2A peer, or dependency | Inventory, provenance check, pin versions/digests, least privilege, dependency review, removal test | Tooling Register, SCA/SBOM where applicable, ADR |
| Confused deputy / excessive agency | Untrusted content triggers a privileged action; agent inherits broad credentials | Human approval for production, destructive, offensive, and data-egress actions; deny-by-default authZ; scoped short-lived credentials; no token passthrough without approval | Approval record, authZ matrix, access register |
| Tool misuse within privileges | Legitimate tool used unsafely: destructive delete, over-broad query, costly API loop, unsafe delegation | Action allowlists, parameter validation, rate limits, dry-run/preview for mutating tools, human approval for irreversible tool calls | Tool call log, approval record, test evidence |
| Data egress to external models/tools | Sending code, Restricted data, secrets, or unapproved production data to external endpoints | No secrets or Restricted data to external AI/model/tool endpoints without Data Owner and Security Authority approval; use approved contracted endpoints; record the data flow | Approval record, ADR, egress config review, data-flow diagram |
| Credential persistence or theft | Long-lived tokens, copied secrets, shared CI credentials, secrets in prompts/logs/artifacts | Short-lived scoped credentials, secrets manager, rotation on exposure or personnel/agent change, no secrets in prompts/logs/artifacts | Access register, scan evidence, rotation record |
| Ledger/evidence tampering | Editing logs, deleting evidence, rewriting history, poisoning memory | Append-only logs, VCS history, restricted stores for sensitive records, independent review, integrity protection for high-assurance logs | Git history, review record, integrity check |
| Goal misgeneralization / scope drift | Extra unrequested work, silent scope change, optimizing for the wrong metric | Stay within the task schema; record deviations; escalate scope changes; human approval for scope changes | Task schema, handoff, `LOG/` |
| Inter-agent protocol abuse | Spoofed agent messages, unauthorized delegation, replayed approvals | Authenticated agent identity where available, message schema with task refs, no approval by assertion alone, log all inter-agent messages | Message log, identity/access register |
| Model output as authority | Treating model/tool output as fact or instruction | Verify outputs independently; never report "clean" without coverage; record limitations; require evidence for claims | `EVD-###` with tool/version and limitations |

## Agent identity and delegation

- Agents act under a named role and permission tier. Delegation must preserve the
  delegator's scope and cannot expand permissions.
- Approvals are bound to a task, action class, target, and time window. A
  standing approval for one action class does not authorize a different class.
- Human approvals MUST be recorded with approver identity, authority, timestamp,
  scope, and expiry. Verbal or implied approval is not sufficient for T3 actions.

## Data-flow rules

- Classify data before sending it to any model, tool, or external endpoint.
- Public/Internal data may use approved endpoints with standard logging.
- Confidential data requires an approved endpoint and data-flow record.
- Restricted data requires Data Owner and Security Authority approval, and
  SHOULD be minimized, masked, or tokenized where possible.
- Secrets are never sent to external model/tool endpoints.

## Incident triggers

Treat as a security incident and preserve evidence when: a tool/agent attempts an
out-of-scope action; embedded instructions are followed; credentials or Restricted
data are exposed; the ledger or evidence is tampered with; or a model/tool claims
a result that cannot be reproduced.
