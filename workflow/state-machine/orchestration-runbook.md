# Orchestration Runbook

> For the Orchestrator and any automation that schedules work from
> `workflow/task-registry.json` plus the project ledger.

## Inputs

- `workflow/task-registry.json` — task graph, roles, skills, gates, feeds.
- `STATE.md` — current statuses, blockers, approvals.
- Ledger registers — defects, incidents, risks, assumptions.
- Human approvals and access grants.

## READY computation

A task is READY when:

1. All `depends_on` tasks are VERIFIED.
2. All `gate_required` gates are approved for the current increment.
3. Required resources/credentials are available and not locked.
4. No higher-priority safety/security blocker exists.
5. Human approvals required by the task or action class are recorded.

Use `scripts/task_readiness.py` for a deterministic check.

## Claiming and locks

- Claim READY tasks by updating `STATE.md` and `LOG/`.
- Acquire resource locks for shared environments, credentials, or write targets.
- Do not claim tasks outside the assigned role/scope.

## Monitoring

Track: READY backlog, IN_PROGRESS age, BLOCKED reasons, gate latency, retry
rates, evidence gaps, cost/egress anomalies, and ledger freshness.

## Escalation

Escalate immediately for missing authority, circular dependencies, stale or
conflicting evidence, suspected injection/tooling compromise, secret exposure,
production/data access needs, destructive actions, or gate bypass requests.

## Gate dossier assembly

When a task `feeds_gates`, collect evidence per
[workflow/gates/review-procedure.md](../gates/review-procedure.md) and the
[gate-dossier checklist](../../checklists/gate-dossier.md). Do not submit stale
or incomplete dossiers.
