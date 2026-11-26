## 13.3 Deployment strategy selection

| Strategy | When to use | Risk and cost | Rollback |
|---|---|---|---|
| Recreate | Non-critical or internal tools. Tolerates downtime | Downtime | Redeploy |
| Rolling | Default for stateless services | Mixed versions briefly. Needs compatibility | Roll back the rollout |
| Blue/green | Needs an instant switch and rollback. Can afford the double capacity | Costlier | Switch the traffic back |
| Canary | High-risk changes, or large user bases. Needs good metrics | Operational complexity | Stop the canary, route to the stable |
| Feature flags (dark launch) | Decouple the deploy from the release | Flag debt, the test combinations | Turn off the flag |
