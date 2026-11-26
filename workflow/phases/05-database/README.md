## PHASE 05 — DATABASE AND DATA ENGINEERING

**Purpose and why.** Data outlives code. Integrity, recoverability, and confidentiality of data are core obligations.

**Roles.** Database Engineer (lead), Backend Developer, Security Engineer, DevOps Engineer.
**Skills.** Cat 7, 14, 19, 22, 12.

### Tasks

| ID | Task and objective | How to execute | Outputs | Validation |
|---|---|---|---|---|
| P05-T01 | **Database selection.** | Decide from access patterns, consistency needs (ACID vs. eventual), query complexity, scale, operational skills, and cost. **Default: a mature relational database** unless a measured need favors document, key-value, wide-column, graph, search, or time-series stores. Polyglot persistence needs an ADR per store. | Selection ADR | Scored matrix. Operational ownership defined. |
| P05-T02 | **Data modeling and ERD.** | Create conceptual, logical, and then physical models. Normalize to 3NF by default. Denormalize only for a measured read need, with a documented consistency strategy. Define keys (surrogate vs. natural, UUIDv7 or sequential trade-offs), constraints (PK, FK, UNIQUE, CHECK, NOT NULL), types, and enum strategies. Map each entity to its owning module and data class. | ERD, data dictionary | Each table has an owner and a classification. Each REQ-F data need is covered. |
| P05-T03 | **Schema implementation and migrations.** | Versioned, forward-only migrations in source control. Use **expand/contract** (backward-compatible) for zero-downtime changes: add, dual-write, backfill, switch reads, and then drop in a later release. Migrations are idempotent, reviewed, and tested on production-like data volume. The migration role is distinct from the runtime role. Include a rollback or compensating plan. | Migration scripts, runbook | Apply-on-empty and apply-on-snapshot tests pass. Timing measured. |
| P05-T04 | **Indexing and query optimization.** | Index from real query patterns (`EXPLAIN`/`EXPLAIN ANALYZE`). Consider composite order, covering and partial indexes. Watch the write overhead. Remove unused indexes. Prevent N+1 queries. Use keyset pagination for large sets. Set statement timeouts. | Index plan, query report | Top queries meet latency targets at projected volume (load tested). |
| P05-T05 | **Transactions, concurrency, integrity.** | Choose isolation levels deliberately. Use optimistic locking (version column) or pessimistic locking where needed. Prevent lost updates and double spends with constraints and atomic statements. Keep transactions short. Consider the outbox pattern. Define deadlock handling and retries. | Concurrency design, tests | Concurrency tests (parallel writes) demonstrate invariants. |
| P05-T06 | **Database security.** | See the controls below. | Hardened DB config | DB security checklist complete. |
| P05-T07 | **Backup, recovery, replication, partitioning.** | Backups per RPO. Follow **3-2-1** (3 copies, 2 media, 1 offsite or immutable). Encrypt and access-control backups. **Restore tests** on a schedule. PITR where RPO requires it. Replication for availability or read scaling, not as a substitute for backup. Partition or shard only on measured need (an ADR). | Backup and DR runbook, restore test report | A successful restore with measured RTO. Data integrity checks after restore. |
| P05-T08 | **Retention, deletion, data lifecycle.** | Implement retention schedules per policy. Support deletion and anonymization workflows (including backups' expiry and derived data). Soft delete only if justified, and note the privacy impact. | Retention config, deletion jobs | A deletion test proves data removal across stores and caches. |
| P05-T09 | **Caching strategy and data verification.** | Cache-aside by default. Define TTLs, invalidation, stampede protection, and key namespacing per tenant. Do not cache secrets or cross-user data in shared keys. Run integrity checks (constraint validation, orphan detection). | Cache design, verification report | Cache poisoning and cross-tenant tests pass. |

**Database security controls (P05-T06)**

| Control | Requirement |
|---|---|
| Access control | Separate accounts for runtime, migration, read-only reporting, and admin. The runtime account has no DDL and no superuser. Per-service credentials. Network-restricted (private subnet, allowlist). Row-level security where it adds defense for multi-tenancy. |
| SQL injection | Parameterized queries only. Stored procedures do not build dynamic SQL from input. The least-privileged account limits impact. |
| Encryption | TLS in transit (verify certificates, no `sslmode=disable`). Encryption at rest (volume or TDE) plus field-level or envelope encryption for Restricted data. Keys in a KMS, with rotation. |
| Credentials | Secrets manager. Dynamic short-lived DB credentials where supported. No defaults. Rotate on staff or agent change. |
| Masking | Production data is not copied to non-prod. Use synthetic or irreversibly masked data. Dynamic masking for support roles. |
| Auditing | Log DDL, privilege changes, and access to Restricted tables. Logs are tamper-resistant and shipped off-host. |
| Retention and deletion | Enforced per §P05-T08. |
| Backup protection | Encrypted, access-restricted, immutable copies, with integrity verification. |
| Hardening | CIS Benchmark for the DB engine, disable unused features, and patch within the SLA (§2.3). |

**Validation and acceptance.** The ERD matches the deployed schema (automated drift check). The restore test is successful, and measured RTO and RPO are within targets. 0 string-concatenated queries (SAST). Runtime account verified without DDL privileges. The top-N queries meet targets.
**Deliverable.** Documented, optimized, secure database architecture and implementation.
**Failure handling.** A failed migration is halted, and the rollback or compensating plan is executed in non-prod first. A production migration failure requires a human decision (NN-04).
**Transition.** Continuous integration with P04 and the P08 pipeline (migration stage).

---
