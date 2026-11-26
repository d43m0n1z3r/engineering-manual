# Agent Memory (Graphify)

This file records the project's agent-memory convention. When the project
uses [Graphify](https://github.com/Graphify-Labs/graphify) — the `/graphify`
skill that turns the repository into a queryable knowledge graph — agents
MUST use it together with, never instead of, the ledger files in this
directory.

## Rules

- **Query before editing.** Before changing code, query the graph for facts
  tied to the affected paths, symbols, and domain: `graphify query`,
  `graphify path`, `graphify explain`, the `--wiki` `index.md`, or the MCP
  server (`graphify --mcp`).
- **Refresh after every change.** After every addition, change, or fix, update
  the graph in the same change set as the ledger update: `graphify . --update`
  (re-extracts only changed files), or rely on the configured `--watch`
  process or post-commit hook (`graphify hook install`).
- **Ledger first.** Facts that affect state, traceability, or approvals live
  in `STATE.md`, `RTM.md`, `DECISIONS/`, and `EVIDENCE/` regardless of the
  graph.
- **No secrets.** The graph is built from repository content; do not add
  secrets, credentials, or restricted data to the corpus it indexes.

## Graph location

- Output: `graphify-out/` (`graph.json`, `GRAPH_REPORT.md`, optional
  `--wiki`, `graph.html`)
- Install: `pip install graphifyy && graphify install` (the PyPI name is
  temporarily `graphifyy`; the CLI and `/graphify` skill are `graphify`)
- Configured: <yes/no, date, verified by>
