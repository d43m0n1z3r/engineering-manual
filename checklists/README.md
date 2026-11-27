# PART 19 — ENGINEERING CHECKLISTS

> Check an item only with evidence. "N/A" requires a justification. Each item
> should point to an evidence ID, artifact path, or explicit review note.

## How to use

- Use the checklist matching the task or gate. A task may require more than one.
- Mark `- [x]` only when evidence exists; otherwise leave `- [ ]` or mark N/A
  with a reason.
- Findings become defects, vulnerabilities, risks, or CCRs; do not bury them in
  checklist comments.
- Reviewers verify a sample of checked items against the cited evidence.

## Checklist index

| Checklist | Use for | Primary reviewer |
|---|---|---|
| [requirements.md](requirements.md) | Requirements quality and completeness | Project Analyst / Technical Reviewer |
| [architecture-threat-model.md](architecture-threat-model.md) | Architecture and threat model review | Software Architect / Security Engineer |
| [code-review.md](code-review.md) | Code and PR review | Technical Reviewer |
| [frontend.md](frontend.md) | UI/UX/frontend changes | UI/UX Engineer / Frontend Developer |
| [backend-api.md](backend-api.md) | API and backend changes | Backend Developer / Security Engineer |
| [database.md](database.md) | Schema, migration, query, and data changes | Database Engineer |
| [security-validation.md](security-validation.md) | Security validation and remediation | Security Engineer |
| [release-readiness.md](release-readiness.md) | Release candidate readiness | QA / DevOps / Release Authority |
| [operations.md](operations.md) | Operational readiness and runbooks | DevOps / Operations |
| [agent-self-check.md](agent-self-check.md) | Agent task self-check before review | Task executor |
| [definition-of-done.md](definition-of-done.md) | Task/gate completion | Reviewer / Orchestrator |
| [agent-ecosystem.md](agent-ecosystem.md) | Agent skills, MCP servers, plugins, hooks, and tool egress | Security Engineer / Engineering Authority |
| [gate-dossier.md](gate-dossier.md) | Gate evidence package completeness | Gate approval authority |
| [ledger-integrity.md](ledger-integrity.md) | Ledger, evidence, and traceability integrity | Technical Reviewer / Orchestrator |
| [supply-chain.md](supply-chain.md) | Dependencies, SBOM, signing, provenance, CI supply chain | Security Engineer / DevOps |
| [data-protection.md](data-protection.md) | Classification, masking, retention, egress, privacy | Data Owner / Security Engineer |
