# PART 12 — DOCUMENTATION REQUIREMENTS

## 12.1 Required documents

| Document | Owner | Update trigger | Location | Reviewer |
|---|---|---|---|---|
| Requirements Specification and RTM | Project Analyst | Any scope or requirement change | `/docs/requirements` | Technical Reviewer |
| Architecture Specification, diagrams (C4, DFD, deployment) | Architect | Any structural change | `/docs/architecture` | Reviewer, Security |
| ADRs | Author of the decision | Every significant decision | `/docs/adr` | Architect |
| Threat Model | Security Engineer | Any trust boundary or the design change, and annually | `/docs/security` (restricted) | Security Authority |
| API reference and the contract | Backend | Each API change | Generated from the contract | Reviewer |
| Data dictionary and ERD | Database Engineer | Each migration | `/docs/data` | Reviewer |
| Design system and UX specs | UI/UX | Design changes | `/docs/design` | Reviewer |
| Test Plan and Reports | QA | Each release | `/docs/testing` | Engineering Authority |
| Security Assessment Report and Vulnerability Register | Security | Each assessment, continuous for the register | Restricted | Security Authority |
| Runbooks, on-call guide | DevOps | Any operational change | `/docs/ops` | Reviewer |
| IR Plan and DR Plan | Security, DevOps | Annually and after the drills and the incidents | `/docs/ops` | Authorities |
| Release notes and the Deployment Report | DevOps | Each release | `/docs/releases` | Release Authority |
| README and the contributing guide | All | Onboarding-relevant changes | Root | Reviewer |
| Agent Capability Register | Orchestrator | Agent changes | `/docs/agents` | Engineering Authority |
| Handoff packets and execution logs | Every agent | Each task | `/HANDOFFS`, `/LOG` | Orchestrator |

## 12.2 Documentation standards
1. **Docs-as-code**: in the repository, reviewed with the code, and versioned.
2. Every document has a header: owner, version, status, last-reviewed date, and the linked requirement IDs.
3. Diagrams are text-based (Mermaid, PlantUML, or Structurizr) where possible.
4. State the **why**, not only the what.
5. A documented procedure is **executable**: the commands are copy-pastable, and the expected outputs are shown. Docs that refer to secrets never contain them.
6. Documents containing the vulnerability details or the sensitive architecture are access-restricted.
