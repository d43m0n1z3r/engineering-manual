## 13.4 Illustrative hardened CI job (pattern, not a prescription)

```yaml
# Pattern illustrating: least-privilege token, pinned action, no secrets for forks
permissions:
  contents: read          # default deny; elevate per job only if required
jobs:
  build:
    runs-on: ephemeral-runner
    steps:
      - uses: org/checkout-action@<full-commit-sha>   # pinned by SHA, not by tag
      - run: install --frozen-lockfile               # deterministic dependency install
      - run: test --ci
      - run: secret-scan --redact
      - run: sast --fail-on high
      - run: sbom generate && sign-artifact          # attestations
  deploy-prod:
    needs: build
    environment: production          # protected: required human approval
    permissions: { id-token: write } # OIDC for short-lived cloud credentials
```
