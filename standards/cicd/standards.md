## 13.2 Standards table

| Area | Required standard |
|---|---|
| Branching | Trunk-based with short-lived branches (≤ 2 days guidance), or the GitFlow with the justification. Protected main. |
| Commits | Atomic, descriptive, linked to the IDs. Signed where policy requires. |
| PR size | Prefer < 400 changed lines. Larger changes are split, or an explicit risk note is added. |
| Review | ≥ 1 independent reviewer. The CODEOWNERS for the sensitive paths. No self-approval. |
| Build | Deterministic. Pinned toolchain. Lockfile install (the frozen mode). |
| Artifact | Immutable and versioned, identified by a digest, signed, with the SBOM and the provenance. |
| Config | Externalized. Validated at startup (fail fast). No secrets in the artifacts. |
| Secrets in CI | Obtained via OIDC federation and short-lived. Not exposed to the untrusted forks. Masked in the logs. |
| Third-party CI components | Pinned to a full commit SHA or digest. Reviewed. |
| Runners | Ephemeral and isolated. Production deployment runners are separated from the build runners. |
| Environments | dev → staging → production, isolated by the accounts, the networks, and the credentials. Staging mirrors production's topology and configuration. |
| Migrations | Forward-only, backward-compatible (expand/contract). Run by a separate step with the migration role, preceded by the verified backup. |
| Rollback | Automated, rehearsed, and with a time target. The previous artifact is retained. |
| Observability of the pipeline | Pipeline run logs and audit logs are retained and monitored. |
