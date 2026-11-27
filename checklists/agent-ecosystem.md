# Agent Ecosystem Checklist

Use before enabling agent skills, MCP servers, plugins, hooks, A2A peers, or
external model/tool endpoints, and after any change to them.

- [ ] Tooling Register entry exists with source, version/SHA, owner, permissions, egress, and status.
- [ ] Provenance reviewed: official source, signed package, or documented fork.
- [ ] Version pinned to commit SHA, immutable tag, or digest.
- [ ] Permissions are least-privilege; no wildcard scopes or token passthrough.
- [ ] Dependencies inventoried and reviewed.
- [ ] Network egress endpoints explicit and approved.
- [ ] Tool descriptions/schemas/return values treated as untrusted input.
- [ ] No secrets or Restricted data required for normal operation.
- [ ] Data classification decided before sending data to the tool/endpoint.
- [ ] Approval recorded for installation/enablement and for material changes.
- [ ] Sandbox/restriction applied where supported.
- [ ] Removal/disable procedure tested.
- [ ] Logging captures tool name, destination class, data class, decision, and approval ref.
- [ ] Change-detection/rug-pull monitoring configured or scheduled.
