## 17.3 Evidence record template

```yaml
id: EVD-0000
task_id: Pxx-Tyy
type: test-report | scan-report | diff | review | approval | benchmark | log
tool_and_version: "<name> <version> | manual review"
command_or_method: "<exact, secrets redacted>"
commit_or_digest: "<sha | sha256:...>"
result_summary: "<pass/fail, counts>"
artifact_location: "<immutable path>"
timestamp_and_actor: "<ISO8601, agent/human>"
limitations: "<what this does NOT prove>"
```
