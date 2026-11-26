## 8.12 Execution logging

Each action that changes state is logged in an append-only structured record:

```json
{"ts":"...","agent":"backend-agent-2","task":"P04-T04","action":"run_tests",
 "command":"<redacted-safe command>","result":"pass","evidence":"EVD-0210",
 "commit":"abc123","permission_tier":"T1","notes":""}
```

Timestamps are UTC ISO-8601. Logs MUST NOT contain secrets or personal data. They record *decisions and reasons* as well as actions, so that a reviewer can reconstruct the "why".

## 8.13 Progress reporting

| Report | Frequency | Content |
|---|---|---|
| Task status update | On each state change | State, the blockers, and the evidence |
| Daily or iteration digest | Daily or per iteration | The completed (verified) tasks, in-progress, blocked, the risks, and the next 24–48 h |
| Gate dossier | At each gate | The evidence index, the criteria checklist with pass or fail, the waivers, and the open risks |
| Risk and vulnerability summary | Weekly | New and closed, and the SLA status |
| Metrics report | Per release | The DORA metrics, the escaped defects, the coverage, and the vulnerability age |

**Honesty rule.** Reports distinguish: *Verified* (evidence), *Done-unverified* (completed, awaiting review), *Assumed* (not tested), and *Not done*. A report must never use "should work" or "likely fine" as a status.
