## PHASE 10 — MONITORING, MAINTENANCE, AND OPERATIONS

**Purpose and why.** Software degrades through dependency drift, new vulnerabilities, load growth, and entropy. Operations keeps the system observable, patched, recoverable, and economical.

**Roles.** DevOps Engineer (lead), Security Engineer, Backend and Database Engineers (on-call responders), Orchestrator.

### Tasks

| ID | Task | How to execute | Outputs | Validation |
|---|---|---|---|---|
| P10-T01 | **Observability foundation** | Three pillars: **metrics** (RED for services: rate, errors, duration. USE for resources: utilization, saturation, errors), **logs** (structured, centralized, with retention by class), and **traces** (distributed, with context propagation, for example OpenTelemetry). Add the correlation ID everywhere. Add error tracking (with PII scrubbing). | Dashboards, log schema | Trace of a sample request spans all components. |
| P10-T02 | **SLOs, alerting, availability and performance monitoring** | Define SLIs and SLOs from the NFRs, with error budgets. Alert on symptoms (user impact), not only causes. Every alert is actionable and has a runbook link. Synthetic probes for availability. | SLO doc, alert rules | An alert-fire test for each critical alert. |
| P10-T03 | **Security event monitoring** | Operate the Phase 06 detections in production. Triage SLAs by severity. Tune false positives. Review audit logs for privileged access. | Security dashboards, triage records | Detection coverage mapped to ATT&CK. Triage SLA met. |
| P10-T04 | **Vulnerability, dependency, and patch management** | Continuous SCA and image scanning. Automated dependency update PRs (with tests). Patch per SLA (§2.3). Track end-of-life dates for runtimes, frameworks, and OS. Emergency patch path (expedited gates, not skipped gates). | Vulnerability Register, patch log | SLA compliance rate is reported monthly. |
| P10-T05 | **Backup verification and disaster recovery testing** | Automated restore tests (at least monthly for critical data). A full DR drill at least annually (or per policy). Measure the RTO and RPO. Record the gaps. | Restore and DR reports | Measured values meet the targets, or a remediation plan exists. |
| P10-T06 | **Incident management** | Lifecycle: detect → triage → declare (severity) → contain → eradicate → recover → post-incident review (blameless, with action items tracked to closure). Preserve evidence. Humans own external communication and regulatory notification. | Incident records, PIRs | Every Sev1 and Sev2 has a PIR within 5 business days. |
| P10-T07 | **Capacity planning and cost** | Track the utilization trends and the growth. Forecast. Load-test before the projected limit. Review costs (FinOps) for waste. | Capacity report | Headroom policy met (for example peak utilization below 70%). |
| P10-T08 | **Technical debt management** | Keep a debt register (item, impact, cost of delay, proposed fix). Reserve capacity (for example 15–20% by default) for debt. Prioritize by risk and by change-frequency hotspots. | Debt register | Debt trend reported each cycle. |
| P10-T09 | **Operational documentation** | Runbooks per alert and per failure mode, an on-call guide, an architecture "as-built", and a maintenance calendar. | Ops docs | A new agent or human can execute a runbook without extra help (verified by a dry run). |

**Deliverables.** Operational documentation, monitoring dashboards, incident records, maintenance plan. Operational details are in Part 14.

---
