### 6. Backend Engineering

| Skill | Description and knowledge | Practical competencies | Tools | Applied in | Level | Validation |
|---|---|---|---|---|---|---|
| Server application architecture | Layering, dependency injection, configuration, and the request lifecycle | Build a clean modular service | Framework tooling | P04 | R: Backend L4 | CR, PEER |
| Concurrency, async, and resilience | Thread pools, event loops, backpressure, timeouts, retries, idempotency, and circuit breakers | Make the service fault-tolerant and prove it with a fault-injection test | Resilience libraries, chaos tools | P04, P07 | R: Backend L4 | LAB |
| Authentication and session engineering | See the P04-T03 | Implement securely using vetted libraries | IdP, auth libraries | P04 | R: Backend L4 | SEED, CR |
| Authorization engineering | RBAC, ABAC, and ReBAC, object-level checks, and policy engines | Build a central deny-by-default layer with the matrix tests | Policy engines | P04 | R: Backend L4 | TC, SEED |
| Background processing and messaging | Queues, streams, delivery semantics, and DLQs | Design idempotent consumers | Brokers | P04 | R: Backend L3 | LAB |
