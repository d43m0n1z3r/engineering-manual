## 8.11 Human approval matrix

| Action | Approval needed | Approver |
|---|---|---|
| Approving requirements, architecture, and gates G1–G4 | Required | See Part 10 |
| Production deployment, configuration change, and migration | Required, per action | Release Authority |
| Rollback in production | Pre-authorized by the runbook for the defined triggers, and otherwise required | Release or Operations Authority |
| Destructive operations (delete data, drop tables, force-push, and the resource destruction) | Required, always | Engineering Authority and the Data Owner |
| Active security testing (any), exploitation, and out-of-automation scans | Required, with a signed RoE | Security Authority |
| Accessing production data | Required, just-in-time | Data Owner |
| Risk acceptance, gate waivers | Required, time-boxed | The gate's authority |
| Adding a new third-party dependency with a notable risk (low maintenance, unusual permissions, and a copyleft license) | Required | Engineering Authority |
| Spending above the budget limits | Required | Sponsor |
| External communication (breach notification, customer notices) | Required | Humans only |
