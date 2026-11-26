# PART 3 — COMPLETE SDLC WORKFLOW

## 3.1 Lifecycle overview

The workflow is **iterative-incremental**. Phases 03–07 repeat per increment (iteration or release slice) after the first architecture baseline. Phases 01–02 are revisited on significant change. Phases 06, 07, 08, and 10 are continuous in effect.

| Phase | Name | Key inputs | Key deliverable | Exit gate |
|---|---|---|---|---|
| (pre) | Authorization and kickoff | Sponsor request | Charter, authorization, access list | G0 |
| 01 | Discovery and Requirements | Business need | Requirements Specification and Project Definition | G1 |
| 02 | Analysis and Architecture | Approved requirements | Architecture Spec, Diagrams, ADRs, Threat Model | G2, G3, G4 (design portion) |
| 03 | UI/UX and Frontend | Architecture, API contracts | Tested frontend and design specs | G5 per change |
| 04 | Backend and API | Architecture, contracts | Secure functional backend and API | G5 per change |
| 05 | Database and Data | Architecture, data model | Secure, optimized database | G5 per change |
| 06 | Security Engineering and Validation | Build under test | Security Assessment Report, Vulnerability Register, Remediation Plan | G7 |
| 07 | Testing and QA | Increment | Test Plan, suites, reports, Defect Register | G6 |
| 08 | DevOps, Infrastructure, CI/CD | Architecture, build | Reproducible pipeline, documented infrastructure | G8 |
| 09 | Production Release | Release candidate | Verified release and deployment report | G9, G10 |
| 10 | Monitoring and Operations | Live system | Ops docs, dashboards, incident records, maintenance plan | Ongoing |
| 11 | Continuous Improvement | Operational data | Improvement Roadmap | Review cadence |

Part 16 gives the master diagram, and Part 9 gives dependency detail.
