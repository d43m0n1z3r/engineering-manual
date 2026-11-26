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

## Output policy

- `graphify-out/` is generated agent memory. Default: do not commit it to the
  project repository; add it to `.gitignore` and regenerate during onboarding or
  CI (`graphify . --update`) so agents query a current graph.
- Commit `graphify-out/` only when the project approves shared agent memory and
  the indexed corpus contains no secrets, credentials, Restricted data, or
  sensitive architecture. Document the access class, owner, and refresh mechanism
  in this file.
- Treat a committed graph as at least Internal: it can reveal code structure and
  decisions. Prefer regeneration over distributing large graphs in history.
