## 14.3 Patch and vulnerability SLAs
Per §2.3. The agents track the **age of open vulnerabilities** and report the SLA compliance. The patches are applied through the pipeline (tests and the scans still run). The emergency path is in the [gate-bypass policy](../../workflow/gates/bypass-policy.md). The EOL components have a replacement plan *before* the EOL date.
