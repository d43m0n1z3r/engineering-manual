## 6.4 Stack archetypes (starting points, not prescriptions)

| Project archetype | Likely sensible baseline | Avoid unless justified |
|---|---|---|
| Internal CRUD tool, small team | Modular monolith with a mature full-stack framework, PostgreSQL, a managed IdP, a PaaS or a single VM, and basic CI | Microservices, Kubernetes, and a message broker |
| Public SaaS web app | Modular monolith, a relational DB, cache if measured, IdP with MFA, containers on a managed platform, IaC, full DevSecOps, WAF | Premature sharding and a multi-region deployment |
| High-throughput event pipeline | Event-driven components with a stream platform, idempotent consumers, strong observability, and the partitioned storage | A synchronous request chain for the bulk path |
| Regulated data (health, payments) | As SaaS, plus the compliance-driven controls (field encryption, the audit trail, key management, retention), and the formal DR | Third-party SDKs with uncontrolled data egress |
| Public API platform | Contract-first design, an API gateway with the quotas, OAuth scopes, versioning, and developer docs | Unversioned breaking changes |
| Static or content site | Static generation with a CDN, minimal JS, and headers hardened | A server runtime with a DB if not required |

---
