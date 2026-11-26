# PART 13 — CI/CD AND DEPLOYMENT STANDARDS

## 13.1 Pipeline architecture

```mermaid
flowchart LR
    A[Commit / PR] --> B[Pre-merge checks]
    B --> B1[Lint + type check + format]
    B --> B2[Unit + component tests]
    B --> B3[Secret scan]
    B --> B4[SAST]
    B --> B5[SCA + license check]
    B --> B6[IaC scan]
    B1 & B2 & B3 & B4 & B5 & B6 --> C{All pass + review approved?}
    C -- no --> A
    C -- yes --> D[Merge to main]
    D --> E[Build once - hermetic]
    E --> E1[SBOM + sign + provenance]
    E --> E2[Container image scan]
    E1 & E2 --> F[Push to artifact registry - immutable digest]
    F --> G[Deploy to staging]
    G --> H[Migrations dry-run + integration/API/contract tests]
    H --> I[E2E + DAST + perf smoke]
    I --> J{Gates G6/G7/G8 evidence valid?}
    J -- no --> A
    J -- yes --> K[Manual approval: Release Authority]
    K --> L[Deploy to production: canary / blue-green / rolling]
    L --> M[Smoke + health + SLO watch]
    M -- fail --> N[Auto rollback + incident]
    M -- pass --> O[Release complete / hypercare]
```

**Principles.** *Build once, promote the same digest* (never rebuild per environment). Everything is automated, and the production deployment is **only** from the pipeline. Pipeline definitions are code, are reviewed, and are protected by CODEOWNERS.
