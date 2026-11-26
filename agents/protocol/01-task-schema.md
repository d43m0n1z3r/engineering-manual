## 8.1 Mandatory task schema (14 fields)

Every task instance MUST contain all fields. A task instance missing a field is **not executable** and is returned to the Orchestrator.

```yaml
task_id: P04-T04                      # 1. Task ID
name: Authorization (function/object level)   # 2. Task name
objective: >                          # 3. Objective (measurable)
  Every endpoint enforces deny-by-default authZ; every object access verifies entitlement.
preconditions:                        # 4. Preconditions (must all be true to start)
  - G4 approved (evidence: EVD-0123)
  - P04-T02 contract VERIFIED
required_inputs:                      # 5. Inputs (with locations and versions)
  - openapi.yaml@sha:abc123
  - threat_model.md (THR-010..THR-018)
  - authz_policy_design.md
required_skills: [authZ engineering L4, appsec L4]   # 6. Skills
execution_instructions:               # 7. Numbered, unambiguous steps
  - 1. Enumerate endpoints from the contract into authz_matrix.csv
  - 2. Implement the central policy layer...
  - 3. Write tests for each matrix cell...
tools_resources: [framework, test runner, SAST]      # 8. Tools
security_considerations:              # 9. Security
  - Tenant id from session only; no client-supplied owner ids
  - No secrets in test fixtures
expected_outputs:                     # 10. Outputs
  - src/authz/*, tests/authz/*, authz_matrix.csv
validation_criteria:                  # 11. Measurable
  - 100% of endpoints appear in the matrix
  - All matrix tests pass; negative cases return 403/404 as specified
  - SAST: 0 High/Critical
completion_conditions:                # 12. Completion (all required)
  - validation passed AND evidence recorded AND reviewed by independent agent AND handoff written
failure_handling:                     # 13. Failure
  - test failure: fix and rerun (max 3 cycles), else escalate
  - design gap: raise CCR to Architect
next: [P04-T05, P07-T07]              # 14. Next task/transition
```

### Fully expanded example B (security-sensitive)

```yaml
task_id: P06-T09
name: Controlled exploitation of confirmed finding VULN-014 (BOLA on /invoices/{id})
objective: Demonstrate impact with minimum proof; do not access real data.
preconditions:
  - Signed RoE (EVD-0301) naming staging.example.internal in scope
  - Human approval record for exploitation of VULN-014 (EVD-0310)
  - VULN-014 status = Confirmed (not merely Suspected)
required_inputs: [RoE, test_identities (2 synthetic users), VULN-014 reproduction steps]
required_skills: [API pentest L4, ethics/RoE L5]
execution_instructions:
  - 1. Verify target host is on the RoE allowlist; abort if not.
  - 2. Authenticate as synthetic user A; request invoice created by synthetic user B.
  - 3. Record request/response (redact tokens) as evidence; stop at the first proof.
  - 4. Do NOT enumerate other IDs beyond the 2 canary records.
  - 5. Delete any test artifacts created; confirm environment state.
tools_resources: [intercepting proxy (scope-locked), API client]
security_considerations: [no persistence, no exfiltration, rate-limited, evidence encrypted]
expected_outputs: [evidence record, updated VULN-014 with impact, cleanup confirmation]
validation_criteria: [reproducible by a second agent using documented steps, within RoE]
completion_conditions: [evidence stored, reviewed by Security Engineer, cleanup verified]
failure_handling:
  - out-of-scope response or unexpected data: STOP, notify Security Authority, do not continue
  - ambiguity about scope: treat as out of scope and ask
next: [P06-T10]
```
