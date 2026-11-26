## 7.3 Agent permission tiers (least privilege)

| Tier | Capabilities | Typical roles | Granting rule |
|---|---|---|---|
| T0 | Read-only on the repos and docs | Reviewer, Analyst (initial) | Default |
| T1 | Write on feature branches and the workspace. Run local and CI tests. No secrets beyond the test scope. | Developers, QA, UI/UX | Task-scoped |
| T2 | Deploy to dev and staging. Read non-production secrets. Run scoped security scanners. | DevOps, Security | Task-scoped, logged |
| T3 | Production changes, production data access, and active offensive tests outside automation | Only with an explicit human approval per action | Just-in-time, expiring, and the two-person rule |

Credentials issued to the agents are short-lived, scoped, and audited. Agents MUST report the permission they *need*, not the permission they *have*.

---
