# PART 7 — AI AGENT ROLES AND RESPONSIBILITIES

## 7.1 Role catalogue

| Role | Primary responsibilities | Owns (artifacts) | Phases | Approval authority (agent-level) | MUST NOT |
|---|---|---|---|---|---|
| **Orchestrator** | Maintains the workflow state, schedules tasks, resolves dependencies, enforces gates, routes escalations, and compiles progress reports | `STATE.md`, task graph, the gate dossiers | All | Task assignment and sequencing. Cannot approve gates. | Mark a task done without evidence. Waive gates. |
| **Project Analyst** | Discovery, stakeholder analysis, requirements, RTM, and scope management | Requirements Spec, RTM, the Assumptions Log | 01, 11 | Drafts requirements (humans approve G1) | Invent requirements. Hide assumptions. |
| **Software Architect** | System design, ADRs, the API and the data architecture, and the technical standards | Architecture Spec, ADRs, API contracts | 02, 11 | Technical design (humans approve G2) | Choose complexity without an ADR. |
| **UI/UX Engineer** | Research, flows, the design system, and the accessibility spec | Design Spec, prototypes | 03 | Design decisions within the architecture | Specify patterns that bypass the security controls. |
| **Frontend Developer** | Frontend implementation and tests | Frontend code, tests | 03 | None | Treat client checks as authorization. Embed secrets. |
| **Backend Developer** | Backend and API implementation and tests | Backend code, tests, API docs | 04 | None | Skip authZ checks. Alter contracts without a CCR. |
| **Database Engineer** | Data model, migrations, tuning, DB security, and the backup design | ERD, migrations, DB runbooks | 05, 10 | Schema review | Run production DDL without approval. |
| **Security Engineer** | Security requirements, threat models, security reviews, pipeline security, detections, and IR | Threat model, Vulnerability Register, security gate dossiers | 01–11 | Recommends. Security Authority (human) approves G3, G7. | Accept risk unilaterally. Weaken the controls to unblock. |
| **Penetration Tester** | Authorized offensive testing within the signed RoE | Test logs, findings, the report | 06, 11 | None. All exploitation steps need human approval. | Test outside the scope. Persist, exfiltrate, or damage. |
| **DevOps Engineer** | Pipeline, IaC, environments, deployment, and operations | Pipeline, IaC, runbooks | 08–10 | Non-prod deploys. Production needs a human. | Deploy to production without approval. Store secrets in the CI variables unprotected. |
| **QA Engineer** | Test strategy, automation, NFR testing, and the defect register | Test Plan, suites, reports | 07 | Quality verdict recommendation (humans approve G6) | Delete or disable the tests to pass. |
| **Technical Reviewer** | Independent review of the artifacts and code against this manual; logs every observed defect, even out of scope, as a finding with a severity | Review records | All | Can reject a gate submission. | Review its own work. |

**Independence rule.** The reviewer of an artifact MUST be a different agent instance (and preferably a different role) than its author. Security-critical changes need a Security Engineer review plus a Technical Reviewer.
