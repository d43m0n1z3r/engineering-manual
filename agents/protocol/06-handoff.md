## 8.8 Handoff protocol

A **handoff packet** (`HANDOFFS/{task_id}.md`) MUST contain:

| Field | Content |
|---|---|
| Summary | What was done and why, in 5–10 lines |
| Artifacts | Paths and commit SHAs or digests |
| Evidence | EVD IDs |
| Decisions | ADR and decision IDs, and the assumptions made |
| Known issues | Open defects, limitations, and the technical debt incurred (with IDs) |
| Security notes | New attack surface, the controls added, and the residual risks |
| Verification instructions | The exact commands to reproduce the validation |
| Next steps | What the receiving agent should do first |
| Open questions | Unresolved items needing an answer |
| Agent memory | Graphify graph queried before work and refreshed after changes, when configured |

The receiving agent MUST acknowledge and re-run at least the smoke verification before accepting. A handoff that cannot be reproduced is rejected.
