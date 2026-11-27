## 7.3 Agent permission tiers (least privilege)

| Tier | Capabilities | Typical roles | Granting rule |
|---|---|---|---|
| T0 | Read-only on the repos and docs; query approved tools; no writes, no secrets beyond public docs | Reviewer, Analyst (initial) | Default |
| T1 | Write on feature branches and the workspace. Run local and CI tests. No secrets beyond the test scope. | Developers, QA, UI/UX | Task-scoped |
| T2 | Deploy to dev and staging. Read non-production secrets. Run scoped security scanners. Mutate non-production test data within the approved environment. | DevOps, Security | Task-scoped, logged |
| T3 | Production changes, production data access, destructive operations, active offensive tests outside automation, and external egress of Confidential/Restricted data | Only with explicit human approval per action or approved time-boxed runbook | Just-in-time, expiring, and the two-person rule where defined |

## Tier rules

- Agents MUST report the permission they *need*, not the permission they *have*.
- Credentials are short-lived, scoped, and audited. Prefer workload identity or
  OIDC federation over stored long-lived tokens.
- T3 grants are recorded in the Access Register with approver, scope, expiry,
  and revocation procedure.
- A task that needs a higher tier is split or escalated; agents do not silently
  expand their own permissions.
- Agent tooling permissions are part of the tier: an MCP server or plugin that
  can write or egress data is treated as at least T1, and as T3 when it can
  touch production or Restricted data.
- Review T2/T3 grants at task end or expiry; revoke unused access.
