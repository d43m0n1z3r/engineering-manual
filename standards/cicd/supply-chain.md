# Supply Chain and Artifact Integrity Standard

> Applies to dependencies, CI/CD components, build artifacts, agent tooling,
> models/datasets, and release packages.

## Requirements

- Pin dependencies and CI components to immutable versions (commit SHA, digest,
  or immutable tag). No floating `latest`/`*` in release paths.
- Generate an SBOM for release artifacts where required (SPDX or CycloneDX).
- Produce build provenance/attestation where required (SLSA/in-toto class).
- Sign artifacts where policy requires; verify signatures before deploy.
- Review new dependencies for maintenance, permissions, license, and risk;
  record notable approvals.
- Scan dependencies (SCA), secrets, IaC, and containers in CI.
- Keep build and production-deploy credentials separate; prefer OIDC
  federation and short-lived credentials.
- Retain rollback artifacts and rehearse rollback.

## Agent/tooling supply chain

- Inventory agent skills, MCP servers, plugins, hooks, A2A peers, and model/tool
  endpoints in the Agent Tooling Register.
- Vet provenance, pin versions, scope permissions, and review egress before
  enablement. See [agents/tooling-governance.md](../../agents/tooling-governance.md)
  and [checklists/agent-ecosystem.md](../../checklists/agent-ecosystem.md).
- Treat tool descriptions, schemas, and outputs as untrusted input.

## Verification

Evidence: SBOM, provenance/attestation, signature verification output, SCA scan,
CI run link, and approval records. Record tool/version and limitations.
