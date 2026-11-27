## 8.12 Execution logging

Each action that changes state is logged in an append-only structured record:

```json
{"ts":"2026-01-01T00:00:00Z","agent":"backend-agent-2","task":"P04-T04",
 "action":"run_tests","command":"<redacted-safe command>","result":"pass",
 "evidence":"EVD-0210","commit":"abc123","permission_tier":"T1",
 "tool":"ci-runner","tool_version":"2026.1","data_class":"Internal",
 "approval_ref":"","notes":""}
```

Required fields: `ts` (UTC ISO-8601), `agent`, `task`, `action`, `result`.
Recommended: `command` (redacted), `evidence`, `commit`, `permission_tier`,
`tool`, `tool_version`, `data_class`, `approval_ref`, `notes`.

Rules:

- Logs MUST NOT contain secrets, tokens, credentials, or unnecessary personal
  data. Redact before writing.
- Logs record decisions and reasons, not only commands, so a reviewer can
  reconstruct the "why".
- High-assurance logs SHOULD be integrity-protected (hash-chained, exported to
  tamper-evident storage, or anchored to VCS).
- Retain logs per project policy and gate/release requirements; do not delete
  logs to make a result look cleaner.

## 8.13 Progress reporting

| Report | Frequency | Content |
|---|---|---|
| Task status update | On each state change | State, blockers, evidence |
| Daily or iteration digest | Daily or per iteration | Verified tasks, in-progress, blocked, risks, next 24–48 h |
| Gate dossier | At each gate | Evidence index, criteria checklist pass/fail, waivers, open risks |
| Risk and vulnerability summary | Weekly | New/closed, SLA status, aging |
| Metrics report | Per release | DORA metrics, escaped defects, coverage, vulnerability age |
| Agent/tooling report | On tooling change or weekly | Tooling Register changes, approvals, egress calls, anomalies |

**Honesty rule.** Reports distinguish: *Verified* (evidence), *Done-unverified*
(completed, awaiting review), *Assumed* (not tested), and *Not done*. Never use
"should work" or "likely fine" as a status.
