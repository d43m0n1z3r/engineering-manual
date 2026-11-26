## PHASE 02 — SYSTEM ANALYSIS AND ARCHITECTURE DESIGN

**Purpose and why.** Architecture determines whether quality attributes are achievable. Threat modeling at this stage costs a fraction of retrofitting security. The aim is the *simplest architecture that meets the quantified NFRs*.

**Roles.** Software Architect (lead), Security Engineer, Database Engineer, DevOps Engineer, Technical Reviewer.
**Skills.** Cats 9, 8, 7, 12, 14, 19 (Part 5).

### Tasks

| ID | Task and objective | How to execute | Outputs | Validation |
|---|---|---|---|---|
| P02-T01 | **System decomposition and architectural style selection.** | Identify capabilities and domains. Use the **style decision procedure** (below). Record the choice and rejected alternatives in an ADR. | Context diagram, Style ADR | ADR lists ≥ 2 alternatives and trade-offs tied to NFRs. |
| P02-T02 | **Component architecture, service boundaries, DDD (where appropriate).** | Use DDD strategic design when the domain is complex: ubiquitous language, bounded contexts, context map. Define modules with explicit public interfaces. Each module owns its data. Define dependency direction rules (domain does not depend on infrastructure). Do not use tactical DDD (aggregates, and so on) for simple CRUD. | Component diagram (C4 Level 2–3), Context Map, Module Interface Specs | Dependency graph has no cycles. Each module has a single clear responsibility. |
| P02-T03 | **Data flow, system interaction, and API architecture.** | Draw DFDs showing every actor, process, data store, and flow. Choose API styles per use case (REST for resource-centric, GraphQL for client-driven aggregation with depth and cost limits, gRPC/RPC for internal low-latency, async events for decoupling). Define the versioning policy, error model (for example RFC 9457 Problem Details), pagination, idempotency keys, and an OpenAPI/AsyncAPI/Protobuf contract draft. | DFD set, API Architecture, Contract drafts | Every flow is traced to a requirement. Contracts validate with a linter. |
| P02-T04 | **Database, caching, messaging, and integration architecture.** | Choose stores by access pattern and consistency need (see Phase 05). Define cache layers, TTLs, invalidation, and what MUST NOT be cached (tokens, per-user sensitive data in shared caches). Choose messaging semantics (at-least-once and idempotent consumers, ordering needs, dead-letter queues, and outbox pattern for DB-plus-message atomicity). Define integration patterns (adapters or anti-corruption layers for third parties, timeouts, circuit breakers). | Data Architecture, Messaging Design, Integration Design | Each data store has an owner and a failure behavior. Each integration has a failure-mode analysis. |
| P02-T05 | **Infrastructure, scalability, availability, failure handling, DR.** | Select the deployment model by need (single VM, PaaS, containers, orchestrator). Define scaling strategy (vertical first, then horizontal on measured bottleneck), statelessness, and health checks. Define availability design (redundancy, zones) from the SLO. Define RTO and RPO and map them to backup and replication design. Define failure modes (FMEA table) and the degradation strategy. | Infrastructure Architecture, FMEA, DR Plan outline | RTO and RPO are traceable to REQ-N. Every single point of failure is either removed or explicitly accepted by a human. |
| P02-T06 | **Security architecture.** | Define the authN design (OIDC/OAuth 2.x with PKCE for public clients, passkeys/WebAuthn and MFA, service-to-service via mTLS or workload identity). Define the authZ model (RBAC, ABAC, or ReBAC, with *centralized policy enforcement points* and deny by default). Define the secrets and key-management design, the encryption design, the audit-logging design, tenant isolation (if multi-tenant), and the privacy design (minimization, retention, DSR support). Map controls to REQ-S and to defense-in-depth layers. | Security Architecture, Control Map | Every REQ-S is mapped to ≥ 1 control. Critical assets have ≥ 2 independent controls. |
| P02-T07 | **Threat modeling and abuse-case analysis.** | Procedure: (1) Define scope and assets. (2) Build DFDs with **trust boundaries**. (3) Enumerate entry points and the attack surface. (4) Apply STRIDE per element (and LINDDUN for privacy). (5) Add abuse cases from Phase 01 and business-logic abuse (race conditions, workflow skipping, quota abuse, and price tampering). (6) Rate threats (DREAD or CVSS-like, or risk matrix). (7) Assign mitigations to controls and tests. (8) Record residual risk and acceptance. (9) Map to MITRE ATT&CK/CAPEC where useful. | Threat Model (`THR-###`), Attack Surface Inventory, Residual Risk Register | All trust-boundary crossings have threats considered. Each High/Critical threat has a mitigation with a verification test ID. |
| P02-T08 | **Architecture Decision Records.** | One ADR per significant decision: context, decision, alternatives, consequences, security impact, status, and reversibility. ADRs are immutable once accepted and are superseded rather than edited. | ADR set (Part 12 template) | Reviewer confirms each is justified by an NFR or constraint. |
| P02-T09 | **Compile the Architecture Specification, then pass G2, G3, and G4 (design portion).** | Assemble the spec, diagrams (C4 context, container, component, deployment, DFD, sequence for critical flows), and threat model. Update the RTM (requirement ↔ component ↔ control). | System Architecture Specification | See gate criteria G2, G3, G4. |

**Style decision procedure (default guidance)**

| Condition | Recommended style | Justification |
|---|---|---|
| Small team, one deployable unit suffices, domain still evolving | **Modular monolith** (default starting point) | Lowest operational complexity, with module boundaries enforced so that later extraction is possible. |
| Simple CRUD, short lifespan | Plain layered monolith | KISS and YAGNI. |
| Independent scaling or deploy cadence needed for specific modules, mature DevOps, multiple teams | Selective **microservices** (extract only proven candidates) | Operational cost (network failure, observability, data consistency) is only justified by real needs. |
| Asynchronous workflows, high fan-out, decoupled consumers | **Event-driven** components (within either style) | Temporal decoupling. Needs idempotency, ordering, and observability discipline. |
| Spiky or low-duty workloads, minimal ops team | Serverless or PaaS functions (consider limits and lock-in) | Operational cost efficiency. |

Microservices, Kubernetes, and cloud are **never assumed**. Each requires an ADR proving the need.

**Security controls (Phase 02)**
- **[R]** Threat model with trust boundaries before any implementation task (G3).
- **[R]** Centralized, deny-by-default authorization design.
- **[R]** Data classification mapped to storage, transport, and logging rules.
- **[R]** Secrets management and key management design.
- **[R]** Audit logging design for security-relevant events.
- **[C]** Tenant isolation design (multi-tenant).
- **[C]** Zero-trust service-to-service authentication (distributed deployments).

**Validation and acceptance.** 100% of NFRs are mapped to an architectural mechanism. 100% of trust-boundary crossings are analyzed. 0 open Critical threats without mitigation. ADRs exist for every style, datastore, auth, and infrastructure choice. Diagrams are consistent with each other (checked by the Technical Reviewer).

**Deliverables.** System Architecture Specification, Architecture Diagrams, ADRs, Threat Model.
**Failure handling.** If NFRs are unachievable within constraints, return to Phase 01 with a feasibility finding. If the threat model reveals a design flaw, redesign before any code. If reviewers disagree, see conflict resolution (§8.9).
**Transition.** After G2+G3+G4 approval, release P03, P04, and P05 (parallel, contract-first), and start P08 early (pipeline foundations).

---
