## 7.2 Human authorities

| Authority | Approves | Must not delegate to agents |
|---|---|---|
| Product Owner / Sponsor | G1, scope changes, risk acceptance for the business, budget | Final security or production approval |
| Engineering Authority | G2, G4, G5 waivers, ADRs of major impact, destructive operation approval | Waiving critical security criteria |
| Security Authority | G0 offensive authorization, G3, G7, security risk acceptance, RoE, Restricted data egress approval | Approving its own testing without independent evidence |
| Data Owner / Privacy Officer | Data classification, retention, DPIA outcome, production data access, Restricted data egress | Treating agent output as a privacy decision |
| Release Authority | G8 jointly, G9, production deployments, rollbacks | Bypassing failed gate evidence |
| Operations Authority | G10, Sev1 incident declaration, DR drills, production operational changes within runbook | Unbounded production access |

## Authority rules

- Name a primary and an alternate for each authority at G0. If the primary is
  unavailable, the alternate acts; if both are unavailable, dependent work stops.
- Approval records MUST include: authority, approver identity, timestamp (UTC
  ISO-8601), scope, evidence reviewed, conditions, and expiry.
- Authorities may delegate routine approvals only through a documented,
  time-boxed delegation. Delegation cannot expand the delegate's authority.
- Conflicting instructions from two authorities are escalated to the Sponsor;
  agents do not choose the convenient instruction.
- Human approvals for T3 actions are just-in-time unless an approved runbook
  explicitly pre-authorizes a narrow action class.
