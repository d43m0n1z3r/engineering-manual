## 11.4 Reliability and resilience tests

| Scenario | Expected behavior (verified) |
|---|---|
| A dependency times out or fails | The timeouts fire, the circuit opens, the degradation is graceful, and no thread or connection leak occurs |
| Database failover or a restart | The reconnection, no data loss beyond the RPO, and the idempotent retries |
| Message redelivery or duplication | The consumers are idempotent |
| Node or pod termination | The traffic shifts and the sessions survive, if designed to |
| Disk full or the memory pressure | Alerts fire before the failure. The degradation is safe |
| Clock skew and expired certificates | Detected and alerted |
| Restore from a backup | Meets the RTO and the RPO. The data integrity checks pass |
