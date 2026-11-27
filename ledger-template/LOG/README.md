# Execution Logs

Store or link to append-only execution records according to project policy.
Use UTC ISO-8601 timestamps and structured fields (agent, task, action, result,
evidence, commit, permission tier, tool/version, data class, approval ref).

Rules:

- Never log credentials, tokens, or unnecessary personal data.
- Record decisions and reasons, not only commands.
- High-assurance logs should be hash-chained, exported to tamper-evident
  storage, or anchored to VCS.
- Retain per project policy and gate/release requirements.
