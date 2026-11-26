# X-KICKOFF-T03 — Initialize project ledger

> Generated from [workflow/kickoff/README.md](../README.md). This card is a derived
> view of the original task table, not a substitute for the phase guidance.

## Source task and objective

Initialize project ledger

## Execution instructions

Copy `ledger-template/` into the project repository or approved workspace. Confirm `STATE.md`, `ASSUMPTIONS.md`, `GLOSSARY.md`, `RTM.md`, `RISKS.md`, `MEMORY.md`, `DEFECTS.md`, `INCIDENTS.md`, `DECISIONS/`, `EVIDENCE/`, `HANDOFFS/`, `LOG/`, and `RESTRICTED/` exist; keep `RESTRICTED/VULNS.md` in approved restricted storage. If the project uses Graphify, build or update `graphify-out/` and confirm agents can query it.

## Expected outputs

Ledger

## Validation

Files exist and are version controlled; `RESTRICTED/VULNS.md` is access-restricted; `graphify-out/` exists and is current when Graphify is configured.

## Required context and task instantiation

1. Read the [phase or kickoff overview](../README.md) and the
   [source section](../README.md). The source section may contain
   additional requirements, including authorization prerequisites.
2. Instantiate all 14 task fields using the
   [task execution schema](../../../agents/protocol/01-task-schema.md). Specify project-specific
   preconditions, inputs, skills, security considerations, failure handling,
   completion conditions, and transition. Do not invent missing facts.
3. Record validation using the
   [evidence standard](../../../core/04-evidence-standard.md).
4. Request independent review before marking this task verified.

## Source table headings

- Task column: Task
- Execution column: Execution
- Output column: Output
- Validation column: Validation
