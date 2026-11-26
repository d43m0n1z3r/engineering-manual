## 8.3 Task dependency management

1. Dependencies are declared in the task graph (`depends_on`, `gate_required`). The Orchestrator computes `READY` tasks.
2. Types: **hard** (output required), **soft** (a preferable order), **gate** (approval required), **resource** (shared environment or credential).
3. Circular dependencies are an error and are escalated to the Orchestrator.
4. A task whose dependency is re-opened is automatically reverted to `PENDING`, and the downstream agents are notified.

## 8.4 Task prioritization

Order by: (1) **Safety and security blockers** (active incidents, leaked secrets, critical vulnerabilities in production). (2) **Gate-critical-path** tasks. (3) Tasks that **unblock** most downstream work. (4) **Risk-reduction value** (the high-risk items first, so that the uncertainty falls early). (5) **Business value** (MoSCoW). (6) Cost and effort. Priority changes are logged with a reason. Agents do not self-reprioritize across tasks, so they propose a change to the Orchestrator.
