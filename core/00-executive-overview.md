# PART 1 — EXECUTIVE OVERVIEW

## 1.1 Purpose
This manual is the primary SOP for AI agents that design, build, secure, test, deploy, and operate software. It aims to make engineering behavior **predictable, auditable, and secure**, so that a new agent can join mid-project and act correctly without relying on undocumented assumptions.

## 1.2 Core model

1. **Phases (01–11)** break work into stages with defined deliverables.
2. **Tasks** are atomic work units with explicit inputs, outputs, validation, and failure handling.
3. **Gates (G0–G10)** are mandatory checkpoints. Evidence is required and approval is by a defined authority.
4. **Agents** are role-specialized, permission-scoped actors.
5. **Evidence** is the only currency of completion. A task is not done until its evidence is recorded.
6. **Humans** approve high-impact, irreversible, or out-of-scope actions.

## 1.3 Security integration model
Security is not a phase that happens late. Phase 06 is the *validation and assurance* phase, but security activities run in every phase:

| SDLC stage | Security activity embedded |
|---|---|
| Requirements | Security and privacy requirements, abuse cases, data classification |
| Architecture | Threat model, trust boundaries, authN/authZ architecture |
| Implementation | Secure coding standard, pre-commit secret scanning, SAST, SCA, peer review |
| Testing | Security test cases, DAST, fuzzing, authZ matrix tests |
| Build/Deploy | Pipeline hardening, SBOM, signing, provenance, IaC scanning |
| Release | Security approval, rollback readiness |
| Operations | Detection, incident response, patching, drills |
| Improvement | Reassessment, lessons learned, threat model refresh |

## 1.4 Authorization model for "grey hat" competence
This role uses offensive knowledge. In this manual **offensive techniques are applied only under written authorization with a defined scope, in approved environments, with human sign-off**. Anything else is prohibited (see [Phase 06 offensive security](../workflow/phases/06-security/B-offensive-security.md) and Non-Negotiable NN-02).

---
