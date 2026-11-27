# Risk Register

| ID | Risk | Likelihood | Impact | Mitigation | Owner | Trigger | Status |
|---|---|---|---|---|---|---|---|

ID format: `RISK-###`.

Scales (1–5): Likelihood = Rare, Unlikely, Possible, Likely, Almost certain.
Impact = Negligible, Minor, Moderate, Major, Severe.

Status values: OPEN, MITIGATING, ACCEPTED (time-boxed, with authority), CLOSED,
REALIZED.

Rules:

- Security risks use the severity model in `core/03-classifications.md` when they
  map to vulnerabilities; keep business/operational risks here.
- Accepted risk requires the named authority and expiry; agents cannot accept.
- Review weekly and at every gate; update triggers when conditions change.
