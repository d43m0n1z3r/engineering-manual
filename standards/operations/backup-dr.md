## 14.4 Backup and DR standards

| Item | Standard |
|---|---|
| Backup frequency | Derived from the RPO |
| Copies | 3-2-1, with one immutable or offline-equivalent copy |
| Protection | Encrypted, with separate credentials and the access logging |
| Verification | Automated integrity check on each backup. A restore test on the schedule (§14.1). |
| DR drill | Annually, a full-scenario test with the measured RTO and RPO and the findings tracked |
| Documentation | A runbook that a new responder can execute, dry-run verified |
