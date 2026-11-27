# Agent Operations Standard

> Applies when AI agents perform work under this manual at scale: scheduling,
> retries, cost, observability, kill switches, and fleet hygiene.

## Scheduling and state

- The Orchestrator computes READY tasks from `workflow/task-registry.json` and
  the ledger; agents do not self-schedule across tasks.
- Task states follow the lifecycle in `agents/protocol/02-lifecycle.md`.
- Use resource locks for shared environments, credentials, and write targets.
- Serialize ledger writes or merge per-task files; avoid lost updates.

## Retries and failure

- Transient failures: bounded retries with backoff and logging.
- Deterministic failures: diagnose root cause; max fix cycles then escalate.
- Flaky tests/tools: quarantine with owner/deadline; never count pass-on-retry
  as clean without noting it.
- Context loss: reload from ledger; do not guess.

## Cost and egress control

- Track model/tool usage and external calls by task and data class.
- Prefer least-privilege endpoints and approved contracted providers.
- Alert on unusual egress volume, new destinations, or Restricted data attempts.

## Observability

- Log agent actions, decisions, tool calls, approvals, and evidence IDs.
- Monitor queue depth, blocked tasks, retry rates, gate latency, and cost.
- Detect anomalies: repeated failures, scope drift, unauthorized tool calls,
  or evidence gaps.

## Kill switch and containment

- Define how to pause an agent, revoke credentials, disable tooling, and freeze
  a gate submission.
- On suspected compromise: preserve evidence, suspend tooling, notify Security
  Authority, and follow incident response.
