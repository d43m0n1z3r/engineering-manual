## 19.8 Release readiness checklist
- [ ] G6, G7, and G8 are valid for the same digest.
- [ ] There are no open S1 or S2 defects and no Critical or High vulnerabilities (or the signed acceptance).
- [ ] The artifact is signed, and the signature is verified.
- [ ] The migration dry-run passed on the production-like data, and the backup is verified.
- [ ] The production config diff was reviewed.
- [ ] The rollback was rehearsed.
- [ ] The monitoring, the alerts, and the dashboards are ready for this version.
- [ ] The on-call and the communication plans are set.
- [ ] The human Release Authority has approved this release.
