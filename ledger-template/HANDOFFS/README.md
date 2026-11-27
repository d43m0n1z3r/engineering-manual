# Handoffs

Store task handoff packets here as `{task_id}.md` (for example `P04-T04.md`).
Include summary, artifacts/SHAs, evidence IDs, decisions, known issues,
security notes, verification instructions, next steps, open questions, and
agent-memory status when Graphify is configured.

Rules:

- The receiving agent must acknowledge and re-run smoke verification.
- A handoff that cannot be reproduced is rejected.
- Do not paste secrets or Restricted data into handoffs; link to restricted
  storage instead.
