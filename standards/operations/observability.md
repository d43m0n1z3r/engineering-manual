## 14.5 Observability standards

| Signal | Standard |
|---|---|
| Logs | Structured (JSON), with the timestamp, the severity, the correlation and trace IDs, the service and the version. No secrets or raw personal data. The retention by the class. |
| Metrics | RED and USE, the business KPIs, and the SLIs |
| Traces | OpenTelemetry-style context propagation. The sampling set by the cost and the need |
| Alerts | The symptom-based (the SLO burn), each linked to a runbook. Each critical alert tested. The alert fatigue is reviewed |
| Audit logs | The authentication events, the authorization failures, the privileged actions, and the data access to the Restricted classes, the configuration and the permission changes |
