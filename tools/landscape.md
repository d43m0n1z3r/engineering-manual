## 6.3 Technology landscape by concern

> Tier legend: **E** Essential (almost every project needs a tool of this kind), **Rec** Recommended, **Spec** Specialized (specific needs), **Opt** Optional. The named products are *examples*, not mandates.

| Concern | Tool category | Examples | Tier | Selection notes |
|---|---|---|---|---|
| Version control and review | Git and a code-hosting platform | Git with a hosted or self-hosted forge | E | Branch protection and audit logs are needed. |
| Issue and requirements tracking | Tracker | Any tracker supporting links and IDs | E | Must support traceability. |
| Diagrams and docs | Docs-as-code and diagram-as-code | Markdown, Mermaid, PlantUML, Structurizr | E | Diff-able text over binary files. |
| Frontend | Frameworks and libraries | React, Vue, Svelte, Angular, or server-rendered templates; or plain HTML for simple sites | E (one) | Choose by team skill and need. Prefer one with auto-escaping. |
| Frontend tooling | Type checker, linter, bundler, component workbench | TypeScript, ESLint, Vite or equivalent, Storybook or equivalent | Rec | Strict typing reduces defects. |
| Backend runtimes | Language and framework | Java/Kotlin (Spring), C# (.NET), Go, Python (Django, FastAPI), Node.js/TypeScript (Express, Nest, Fastify), Ruby (Rails), PHP (Laravel), Rust (Axum, Actix) | E (one) | A mature framework with built-in security features (authZ, CSRF, ORM) is preferred over a micro-framework with a pile of plugins. |
| API tooling | Contract and docs | OpenAPI and linters, AsyncAPI, Protobuf and Buf, GraphQL SDL | E | Contract-first. |
| Relational DB | RDBMS | PostgreSQL, MySQL/MariaDB, SQL Server, Oracle, SQLite (embedded and small) | E | Default to a relational DB. |
| NoSQL and specialized | Document, KV, search, graph, TSDB | MongoDB, Redis or Valkey, Elasticsearch or OpenSearch, Neo4j, TimescaleDB | Spec | Justify through the access pattern. |
| Messaging | Brokers and streams | RabbitMQ, Kafka, cloud queues, NATS | Spec (when async needed) | Do not add one without an async requirement. |
| Identity | IdP and libraries | A managed IdP or a self-hosted one such as Keycloak, framework auth modules, OAuth and OIDC libraries | E | Avoid writing your own. |
| Secrets and keys | Vault and KMS | HashiCorp Vault or OpenBao, cloud secrets managers and KMS, SOPS | E | |
| Containers | Build and runtime | OCI images and a container engine | Rec | Skip when a simple VM or PaaS suffices. |
| Orchestration | Orchestrator | Kubernetes, Nomad, managed container platforms | Spec | ADR-justified. Operational cost is high. |
| IaC | Provisioning and config | Terraform or OpenTofu, Pulumi, Ansible, CloudFormation | E (for non-trivial infra) | |
| CI/CD | Pipeline system | Any mainstream CI system | E | Needs OIDC, protected environments, and isolated runners. |
| Observability | Telemetry | OpenTelemetry, Prometheus-style metrics, centralized log stack, tracing backend, error tracker | E (logs and metrics), Rec (traces) | Scrub PII. |
| Testing: unit and integration | Frameworks | The ecosystem standard for the language, plus ephemeral containers for dependencies | E | |
| Testing: E2E | Browser automation | Playwright, Cypress, Selenium | Rec | Limit to critical journeys. |
| Testing: performance | Load tools | k6, Gatling, JMeter, Locust | Rec | |
| Testing: contract | Consumer-driven contracts | Pact or schema-based | Spec | Multi-service. |
| Testing: accessibility | Automated a11y | axe-core and similar | E (UI projects) | |
| SAST | Static analysis | Semgrep, CodeQL, SonarQube, language-native analyzers | E | At least one, with custom rules for project-specific risks. |
| SCA and SBOM | Dependency scanning | OSV-based scanners, Dependabot or Renovate, Trivy, Grype, Syft, OWASP Dependency-Check | E | |
| Secret detection | Scanners | gitleaks, trufflehog, platform push protection | E | Pre-commit, CI, and history. |
| Container and IaC scanning | Scanners | Trivy, Grype, Checkov, tfsec-class tools, kube-linters | E (if used) | |
| DAST | Dynamic scanners | OWASP ZAP, Burp Suite, Nuclei (templates reviewed) | Rec | Staging only, and within the RoE. |
| Pentest toolkit | Manual and framework | Intercepting proxies, Nmap-class scanners, API clients, and the exploitation frameworks (lab or in scope) | Spec | Restricted to the Penetration Tester agent under a signed RoE. |
| Fuzzing | Fuzzers | Language-native fuzzers, AFL-class, schema-based API fuzzers | Spec | |
| Network analysis | Capture and analysis | Wireshark, tcpdump, flow logs | Spec | |
| Security monitoring | SIEM, EDR, WAF | Open-source or commercial log analytics, EDR on hosts, WAF at the edge | Rec (scale-dependent) | Scale to the risk. A small system can use centralized logs with alerts. |
| Hardening benchmarks | Compliance scanners | CIS-CAT-class tools, OpenSCAP, kube-bench, Lynis | Rec | |
| Supply chain | Signing and attestation | Sigstore/cosign, in-toto, SLSA tooling | Rec | |
| Threat modeling | Tools | OWASP Threat Dragon, Microsoft TMT, or docs-as-code | Rec | |
