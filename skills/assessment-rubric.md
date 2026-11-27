# Agent Skill Assessment Rubric

> Use this rubric when validating an agent's proficiency for a role or task.
> Record results in the Agent Capability Register.

## Evidence types by level

| Level | Minimum evidence |
|---|---|
| L1 | Accurate explanation of concepts; can follow a documented procedure with supervision. |
| L2 | Correct completion of routine guided exercises; uses reference material. |
| L3 | Independent delivery on typical tasks; diagnoses common failures; work passes review with few defects. |
| L4 | Handles complex/ambiguous problems; designs solutions; reviews others' work; reduces defect classes. |
| L5 | Defines practice; handles novel/edge cases; makes systemic decisions; authors standards or novel solutions. |

## Validation methods

- **CR** — review a sample of the agent's work for correctness, security, and
  convention adherence.
- **LAB** — run a sandbox exercise with known-answer tests and seeded defects.
- **TC** — require tests to pass on a standard task without weakening checks.
- **DOC** — review produced artifacts for completeness, accuracy, and traceability.
- **SEED** — detect planted defects/vulnerabilities; measure false positives/negatives.
- **DRILL** — participate in an operational drill (incident, release, restore).
- **SCEN** — answer scenario questions including ambiguous and adversarial cases.
- **PEER** — peer review by a higher-level agent or human authority.

## Exercise design rules

- Include negative cases, ambiguous inputs, and out-of-scope requests.
- Do not reward confident wrong answers; require evidence and limitations.
- For security skills, include prompt-injection, tool-poisoning, data-egress, and
  unauthorized-action scenarios.
- Record tool/model version, prompt/task set digest, and environment where
  relevant.

## Result recording

For each assessment record: agent/role, skill category/row, claimed level,
method, artifact/exercise ID, date, validator, result (`pass`, `conditional`,
`fail`), limitations, and next review date. Conditional results specify the
supervision or re-test required.
