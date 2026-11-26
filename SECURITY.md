# Security Policy

This repository is documentation and process guidance. It describes offensive
security testing, but the repository itself has no production service to attack.
Do not run offensive techniques against real systems while reviewing it.

## Reporting a vulnerability

Report suspected vulnerabilities in this manual — for example unsafe guidance,
a missing safety control, exposed secrets, or a CI/check bypass — through GitHub
private vulnerability reporting (Security Advisories) for this repository. If
private reporting is unavailable, open a minimal public issue that describes the
concern without exploit details and ask for a private channel.

Do not include secrets, personal data, or working exploit material in the
report. For vulnerabilities in systems *described* by the manual, follow that
project's own Rules of Engagement and incident process instead.

## Scope

- In scope: this repository's content, `scripts/`, CI workflows, and the ledger
  templates.
- Out of scope: third-party standards referenced by the manual, target systems
  in user projects, and social engineering of maintainers.
