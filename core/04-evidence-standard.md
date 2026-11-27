## 2.4 Evidence standard (applies to all tasks)

An **evidence record** (`EVD-###`) MUST contain:

| Field | Description |
|---|---|
| id | Unique evidence ID |
| task_id | Task that produced it |
| type | test-report, scan-report, diff, log-excerpt, screenshot, approval, benchmark, review, config-export, attestation |
| tool_and_version | Exact tool name, version, and configuration (or "manual review") |
| command_or_method | The exact command or procedure (secrets redacted) |
| commit_or_build_ref | Commit SHA or artifact digest the evidence applies to |
| result_summary | Pass/fail and counts |
| artifact_location | Immutable path or link |
| timestamp_and_actor | When and by which agent or human (UTC ISO-8601) |
| limitations | What the evidence does NOT show |

Evidence is **stale** if the commit or artifact it refers to has changed in a
way that could invalidate it. Stale evidence MUST be regenerated before gate
review.

## Storage, retention, and integrity

- All timestamps are UTC ISO-8601.
- Choose storage class by data classification: Public/Internal evidence may live
  in `EVIDENCE/`; Confidential and Restricted evidence, exploit details, and
  sensitive architecture live in restricted storage with access logging.
- Retention follows project policy and the referenced gate or release;
  sensitive evidence is not retained longer than needed.
- Append-only execution logs SHOULD be integrity-protected (hash-chained,
  exported to tamper-evident storage, or anchored to VCS) for high-assurance
  projects.
- Redact secrets, tokens, and unnecessary personal data before storing evidence.
- Evidence MUST identify coverage and limitations; a partial scan is not a clean
  bill.
