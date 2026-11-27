# Gate Review Procedure

> Use for every gate G0–G10. The gate file defines entry, evidence, criteria,
> rejection conditions, remediation, and approval authority; this procedure
> standardizes how the dossier is assembled and decided.

## Dossier contents

- Gate ID, phase/increment, process profile, and entry criteria status.
- Evidence index: EVD IDs, locations, tool/version, commit/artifact refs,
  timestamps, and limitations.
- Criteria checklist: each criterion marked pass/fail/N/A with evidence ref.
- Waivers: reason, compensating control, owner, expiry, approver.
- Open risks, defects, vulnerabilities, and assumptions affecting the decision.
- Human approvals and access grants relevant to the gate.
- Reviewer independence statement.

## Freshness and validity

- Evidence must be current for the commit/artifact under review.
- Stale evidence is regenerated or explicitly marked not usable.
- "Reported, not evidenced" items cannot satisfy a criterion.
- Restricted evidence is referenced by location, not copied into open storage.

## Decision rules

- PASS requires all required criteria met with current evidence and the named
  approval authority's recorded approval.
- CONDITIONAL PASS is allowed only for non-critical criteria with a documented,
  time-boxed waiver and compensating control.
- Critical security criteria cannot be waived by agents; only the Security
  Authority may waive them, and only per policy.
- REJECT returns work with findings; record remediation owner and next gate.
- ESCALATE when authority is unclear, evidence conflicts, or scope is exceeded.

## After the decision

- Record the decision in `STATE.md`, the gate dossier, and `LOG/`.
- Update RTM/risks/defects as needed.
- Notify downstream owners; blocked tasks remain blocked until the gate clears.
