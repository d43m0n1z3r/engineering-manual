## 2.4 Evidence standard (applies to all tasks)

An **evidence record** (`EVD-###`) MUST contain:

| Field | Description |
|---|---|
| id | Unique evidence ID |
| task_id | Task that produced it |
| type | test-report, scan-report, diff, log-excerpt, screenshot, approval, benchmark, review |
| tool_and_version | Exact tool name, version, and configuration (or "manual review") |
| command_or_method | The exact command or procedure (secrets redacted) |
| commit_or_build_ref | Commit SHA or artifact digest the evidence applies to |
| result_summary | Pass/fail and counts |
| artifact_location | Immutable path or link |
| timestamp_and_actor | When and by which agent or human |
| limitations | What the evidence does NOT show |

Evidence is **stale** if the commit or artifact it refers to has changed in a way that could invalidate it. Stale evidence MUST be regenerated before gate review.

---
