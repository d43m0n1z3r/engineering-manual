# Supply Chain and CI Security Checklist

Use for dependencies, build pipelines, artifacts, SBOM/provenance, and agent
tooling supply chain.

- [ ] Dependencies pinned; lockfiles used; no floating `latest`/`*` in release paths.
- [ ] New dependencies reviewed for maintenance, permissions, license, and risk.
- [ ] SBOM generated for release artifacts where required.
- [ ] Build provenance/attestation present where required (SLSA/in-toto class).
- [ ] Artifacts immutable, versioned, digest-addressed, and signed where policy requires.
- [ ] CI uses OIDC/federation and short-lived credentials; no long-lived secrets in variables.
- [ ] Runners ephemeral/isolated; production deploy separated from build.
- [ ] Third-party CI actions/components pinned to SHA/digest and reviewed.
- [ ] Secret scanning, SCA, IaC scanning, and container scanning run in CI.
- [ ] Agent skills/MCP/plugins/hooks inventoried and vetted per agent ecosystem checklist.
- [ ] Rollback artifact retained and rehearsal evidence available.
