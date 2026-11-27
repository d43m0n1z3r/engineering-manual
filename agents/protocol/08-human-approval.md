## 8.11 Human approval matrix

| Action | Approval needed | Approver |
|---|---|---|
| Approving requirements, architecture, and gates G1–G4 | Required | See Part 10 |
| Production deployment, configuration change, and migration | Required, per action or approved runbook | Release Authority |
| Rollback in production | Pre-authorized by runbook for defined triggers, otherwise required | Release or Operations Authority |
| Destructive operations (delete data, drop tables, force-push, resource destruction) | Required, always; two-person rule where defined | Engineering Authority and Data Owner |
| Active security testing, exploitation, out-of-automation scans | Required, with signed RoE | Security Authority |
| Accessing production data | Required, just-in-time | Data Owner |
| Risk acceptance, gate waivers | Required, time-boxed | The gate's authority |
| New third-party dependency with notable risk | Required | Engineering Authority |
| External AI/model/tool endpoint for Confidential/Restricted data | Required | Data Owner and Security Authority |
| Installing/enabling agent skills, MCP servers, plugins, hooks, or A2A peers | Required | Engineering Authority; Security Authority if data/egress/permissions are material |
| Spending above budget limits | Required | Sponsor |
| External communication (breach notification, customer notices) | Required | Humans only |

## Approval record

Every approval MUST be recorded with: authority, approver identity, timestamp
(UTC ISO-8601), scope, evidence reviewed, conditions, expiry, and revocation
procedure. Verbal or implied approval is insufficient for T3 actions.

## Rules

- Approvals are bound to task, action class, target, and time window.
- Just-in-time grants expire; review at task end or expiry.
- Emergency changes follow [workflow/gates/bypass-policy.md](../../workflow/gates/bypass-policy.md)
  and still require real-time human approval.
- If approval is missing, stop the dependent work and escalate; do not proceed
  on assumption.
