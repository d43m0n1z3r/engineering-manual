# Evidence

Store evidence records here or link to approved immutable evidence storage.
Use `EVD-###` IDs and the evidence standard fields (type, tool/version, command,
commit/artifact ref, result, location, timestamp/actor, limitations).

Rules:

- Do not put secrets, credentials, or unnecessary personal data in evidence.
- Confidential/Restricted evidence goes to restricted storage with access logs.
- Mark stale evidence and regenerate before gate review.
- Prefer append-only, integrity-protected storage for high-assurance projects.
