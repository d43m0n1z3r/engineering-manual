## PHASE 01 — PROJECT DISCOVERY AND REQUIREMENTS ENGINEERING

**Purpose and why.** Defects in requirements are the most expensive to fix later. This phase turns an ambiguous need into a testable, prioritized, bounded definition, including security and privacy needs, so that downstream design is neither over- nor under-built.

**Roles.** Project Analyst (lead), Software Architect (feasibility), Security Engineer (security and privacy requirements), Technical Reviewer.
**Skills.** Requirements elicitation and analysis, domain modeling, risk analysis, privacy and regulatory awareness, technical writing (Part 5: [Cat 4](../../../skills/04-software-engineering-principles.md), [Cat 9](../../../skills/09-system-design-and-architecture.md), [Cat 14](../../../skills/14-application-security.md), [Cat 23](../../../skills/23-technical-documentation-and-engineering-communication.md)).

### Tasks

| ID | Task and objective | How to execute | Outputs | Validation |
|---|---|---|---|---|
| P01-T01 | **Discovery and problem identification.** Define the problem, not the solution. | 1. Gather all provided material. 2. Write the problem statement: who has what problem, impact, and current workaround. 3. Define measurable success outcomes (KPIs). 4. Identify unknowns and list clarifying questions. 5. Ask the human for answers to blocking questions. | Problem Statement, KPI list, Open Questions Log | Each KPI is measurable (baseline, target, method). Blocking questions are answered or turned into logged assumptions. |
| P01-T02 | **Stakeholder analysis.** Know who is affected and who decides. | Build the stakeholder register: role, interest, influence, concerns, approval rights. Include non-obvious stakeholders (security, legal, support, operations, end-user groups, regulators, third-party integrators, and adversaries as *threat actors*). | Stakeholder Register (with power/interest grid) | Every gate approver is present. Every user class maps to at least one persona. |
| P01-T03 | **Elicit business, functional, and non-functional requirements.** | Derive business requirements (outcomes), then functional requirements ("The system SHALL…" with unique IDs). Derive NFRs by quality attribute: performance (p95 latency, throughput), availability (SLO, RTO, RPO), scalability (users, data growth), security, privacy, accessibility, compliance, observability, maintainability, compatibility, and cost. Every NFR MUST be quantified (for example "p95 < 300 ms at 500 rps"). If the stakeholders cannot quantify it, record an assumption and propose a default. | Requirements Catalogue (REQ-F, REQ-N) | No requirement is ambiguous (no "fast", "secure", "user-friendly" without metrics). Each is atomic, testable, and uniquely identified. |
| P01-T04 | **User stories, use cases, acceptance criteria.** | Write stories ("As a ⟨persona⟩ I want ⟨capability⟩ so that ⟨benefit⟩"). Write use cases for complex flows (actors, preconditions, main and alternate flows, postconditions). Write acceptance criteria in Given/When/Then, including negative and abuse paths (unauthorized, invalid input, and rate-exceeded cases). | Story Backlog, Use Case Specs, Acceptance Criteria | Each story has ≥ 1 positive and ≥ 1 negative criterion. Each criterion is automatable or has a documented manual procedure. |
| P01-T05 | **Constraints, assumptions, dependencies, scope boundaries.** | List technical, legal, budget, timeline, staffing, and operational constraints. List assumptions (with owner, validation plan, and impact if wrong). List external dependencies (vendors, APIs, teams). Write in-scope, out-of-scope, and future-scope lists. | Constraints and Assumptions Register, Scope Statement | Out-of-scope is explicit. Each assumption has an owner and expiry. |
| P01-T06 | **Feasibility and technical research.** | Evaluate technical, operational, economic, schedule, and legal feasibility. For each uncertain technology, run a time-boxed spike with a pass/fail criterion. Compare candidates using the weighted matrix (Part 6.2). Verify versions, maintenance status, and licenses from authoritative sources. | Feasibility Report, Spike Results, Technology Shortlist | Every claim has a source or an experiment. No technology is chosen by popularity alone. |
| P01-T07 | **Risk identification.** | Identify risks (technical, security, delivery, operational, compliance, vendor). Score likelihood × impact. Define mitigation, contingency, owner, and trigger. | Risk Register (`RISK-###`) | Top risks have owners and mitigations. High risks are reported to the human sponsor. |
| P01-T08 | **Initial security and privacy requirements.** | Classify data (§2.3). Identify applicable regulations (flag for human/legal confirmation). Define authentication and authorization needs, audit needs, retention and deletion needs, data subject rights, breach notification needs, and encryption needs. Define abuse cases ("As an attacker I want to…"). Map to OWASP ASVS target level (L1/L2/L3) chosen by data sensitivity. Perform a privacy review (data minimization, purpose limitation). | Security and Privacy Requirements (REQ-S, REQ-P), Data Inventory, ASVS target level | Each REQ-S is testable. ASVS level is justified. Data inventory has an owner for each data class. |
| P01-T09 | **Compile Requirements Specification and Project Definition; seed the RTM.** | Consolidate into the specification. Prioritize with MoSCoW. Seed the Requirements Traceability Matrix (RTM) with all IDs. Submit to G1. | Requirements Specification, Project Definition, RTM v0 | Technical Reviewer completes the consistency check (no conflicting requirements, no orphan stories, and glossary defined). |

**Security controls (Phase 01)**
- **[R]** Data classification and data inventory complete.
- **[R]** Abuse cases are written for each high-value asset or function.
- **[R]** ASVS target level chosen.
- **[R]** Regulatory applicability flagged for human confirmation.
- **[C]** Privacy impact assessment (DPIA) if personal data at scale or sensitive categories are processed.

**Tools.** Issue trackers, requirements docs-as-code, diagramming tools, spreadsheet-based decision matrices, threat-intel feeds for domain-specific threats.

**Validation and acceptance (measurable).** 100% of requirements have an ID, a priority, an acceptance criterion, and a verification method. 0 unquantified NFRs. 100% of REQ-S items map to ≥ 1 abuse case or control objective. Stakeholder sign-off recorded.

**Deliverable.** Requirements Specification and Project Definition. **Gate:** G1.
**Failure handling.** Conflicting requirements go to the Product Owner for ruling and are logged as a decision. Stakeholders who do not respond for the defined SLA trigger escalation to the sponsor. A critical unknown becomes a spike or a blocking question, and the agent does not guess.
**Transition.** After G1 approval, go to P02-T01.

---
