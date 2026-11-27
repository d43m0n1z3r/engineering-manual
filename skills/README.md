# PART 5 — DEVELOPER × CYBERSECURITY SKILLS MATRIX

## 5.1 Proficiency scale

| Level | Name | Definition | Typical evidence |
|---|---|---|---|
| 1 | Foundational | Understands concepts and vocabulary, and can follow documented procedures with supervision. | Explains concepts accurately |
| 2 | Beginner Practitioner | Completes routine tasks correctly with reference material. Needs review for non-routine work. | Passes guided exercises |
| 3 | Intermediate | Works independently on typical problems. Diagnoses common failures. Applies best practices. | Delivers reviewed work with few defects |
| 4 | Advanced | Handles complex or ambiguous problems, designs solutions, mentors, and reviews others' work. | Design leadership, reduces defect classes |
| 5 | Expert | Defines the practice, handles novel or edge-case problems, and makes the decisions with systemic impact. | Novel solutions, standards authorship |

**Classification.** **M** = Mandatory for all engineering agents (at the stated minimum level). **R** = Mandatory for the named role only. **S** = Specialized (needed only by projects or roles that require it). **O** = Optional. Not every agent or project needs every specialization.

**Validation methods (key).** *CR*: code review sample. *LAB*: practical exercise in a sandbox. *TC*: tests pass on a standard task. *DOC*: artifact review. *SEED*: seeded-defect detection exercise. *DRILL*: operational drill. *SCEN*: scenario-based questioning. *PEER*: peer review by a higher-level agent.

## 5.2 Skills tables

> Column legend: **Description and knowledge** | **Practical competencies** | **Tools** | **Applied in** | **Level** | **Validation**

The numbered files `01-*.md` through `23-*.md` contain the detailed skill tables.
Each row names the skill, required knowledge, practical competencies, example
tools, phases where it applies, minimum level/classification, and validation
method. Role minimums are summarized in [role-minimums.md](role-minimums.md).

## 5.4 Competency assessment evidence

Skill levels are claims until validated. Validation evidence MUST be recorded in
the Agent Capability Register with: agent/role, skill category and row, claimed
level, validation method, artifact or exercise ID, date, validator, result, and
limitations. See [assessment-rubric.md](assessment-rubric.md) for the rubric.

Rules:

- A level is not self-assigned; independent validation or supervised work is
  required for L3+.
- Seeded-defect and known-answer exercises should include negative cases and
  ambiguous inputs.
- Failed validation places the agent in supervised mode until re-assessed.
- Recertify on role change, major toolchain change, security incident, or at the
  project-defined cadence.

## 5.5 Using the matrix

- Architects and Orchestrators use [role-minimums.md](role-minimums.md) to check
  whether an agent may claim a task.
- Reviewers use the matrix to decide whether a reviewer has enough skill to
  approve security-critical changes.
- Skill gaps are risks or staffing inputs, not silent waivers.
