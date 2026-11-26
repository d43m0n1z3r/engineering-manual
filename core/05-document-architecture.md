# PART 0 — DOCUMENT ARCHITECTURE AND HOW TO USE THIS MANUAL

## 0.1 Document map

| Part | Content | Primary readers |
|---|---|---|
| 1 | Executive Overview | Everyone |
| 2 | Engineering Principles and Standards | Everyone |
| 3 | Complete SDLC Workflow | Orchestrator, Project Analyst |
| 4 | Detailed Procedures, Phases 01–11 | Phase-owning agents |
| 5 | Developer × Cybersecurity Skills Matrix | Agent designers, reviewers |
| 6 | Tools and Technology Reference | Architect, DevOps, Security |
| 7 | AI Agent Roles and Responsibilities | Orchestrator, all agents |
| 8 | AI Agent Execution Protocol | All agents |
| 9 | Workflow Dependencies and State Transitions | Orchestrator |
| 10 | Engineering and Security Quality Gates | Reviewers, approvers |
| 11 | Testing and Validation Standards | QA, all developers |
| 12 | Documentation Requirements | All agents |
| 13 | CI/CD and Deployment Standards | DevOps, Security |
| 14 | Production Operations and Maintenance | DevOps, Security, SRE |
| 15 | Continuous Improvement Framework | Orchestrator, Architect |
| 16 | Master Workflow Diagram | Everyone |
| 17 | Reusable Task Templates | All agents |
| 18 | Definition of Done | All agents |
| 19 | Engineering Checklists | All agents |
| 20 | Reference Standards and Further Reading | Everyone |

## 0.2 Conventions

- **Task ID format:** `P{phase}-T{nn}`, for example `P04-T04`. Cross-cutting tasks use `X-{name}`.
- **Gate ID format:** `G{n}`, defined in Part 10.
- **Requirement ID format:** `REQ-F-###` (functional), `REQ-N-###` (non-functional), `REQ-S-###` (security), `REQ-P-###` (privacy).
- **Other IDs:** `THR-###` (threat), `ADR-###` (decision), `TC-###` (test case), `VULN-###` (vulnerability), `RISK-###` (risk), `EVD-###` (evidence).
- **Inheritance rule:** Each phase section states Skills, Tools, Security considerations, Failure handling, and Transition once. All tasks in the phase inherit them unless a task overrides them. Part 8 defines the full 14-field task schema and gives two fully expanded examples. Agents MUST instantiate the full schema (Part 17) when they create a work item.

## 0.3 Scope, assumptions, and limits of this manual

1. **Technology-agnostic.** Named tools are examples. The Architect selects tools through the decision procedure in Part 6.
2. **Versions.** This manual was written without live access to the internet. Any version-specific claim (standard editions, framework versions, algorithm parameters, CVE status) MUST be verified against the authoritative source at the time of use. The agent MUST record the verification in the ADR or task evidence.
3. **Thresholds are defaults.** Numeric thresholds (coverage, SLAs, and so on) are defensible defaults. A project MAY change them only through an ADR approved at the relevant gate. It MUST NOT silently lower them.
4. **Not legal advice.** Regulatory applicability (GDPR, HIPAA, PCI DSS, and others) MUST be confirmed by a qualified human. Agents flag it but do not decide it.
5. **Missing information.** If a required input is missing, the agent MUST (a) list what is missing, (b) state its assumptions explicitly in the Assumptions Log, (c) ask for clarification when the assumption is high-impact, and (d) never proceed on an assumption that affects security, data handling, or cost without human confirmation.

---
