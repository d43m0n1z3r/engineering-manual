## 8.3 Task dependency management

Dependencies are declared in the task graph (`depends_on`, `gate_required`) and
the machine-readable [task registry](../../workflow/task-registry.json). The
Orchestrator computes `READY` tasks; agents do not self-declare readiness.

Dependency types:

- **Hard** — the upstream output must exist and be VERIFIED before start.
- **Soft** — preferred order only; may be overridden with a logged reason.
- **Gate** — an approval must be recorded before claim.
- **Resource** — shared environment, credential, data set, or write target;
  serialized by lock or reservation.
- **External** — third-party, human, or production prerequisite outside the
  task graph; tracked as a blocker until cleared.

Rules:

1. A task is READY only when all hard dependencies are VERIFIED, all required
   gates are approved, and required resources are available.
2. Circular dependencies are an error and are escalated to the Orchestrator.
3. A task whose dependency is re-opened is reverted to PENDING and downstream
   agents are notified.
4. Resource locks name owner, scope, expiry, and release condition. Locks are
   released on completion, failure, or expiry.
5. Dependency changes after claim require Orchestrator approval and may return
   the task to READY/PENDING.

## 8.4 Task prioritization

Order by: (1) safety and security blockers (active incidents, leaked secrets,
critical vulnerabilities in production); (2) gate-critical-path tasks; (3) tasks
that unblock the most downstream work; (4) risk-reduction value (high-risk items
early); (5) business value (MoSCoW); (6) cost and effort.

Priority changes are logged with reason, evidence, and approver. Agents propose;
the Orchestrator applies within policy; humans decide cross-task or scope
conflicts. Do not reprioritize by silently skipping dependencies.
