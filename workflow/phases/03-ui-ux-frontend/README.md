## PHASE 03 — UI/UX AND FRONTEND ENGINEERING

**Purpose and why.** The frontend is the user's trust surface and a primary attack surface. Usable, accessible, and resilient interfaces reduce user error, support cost, and risky workarounds.

**Roles.** UI/UX Engineer, Frontend Developer, Security Engineer (review), QA Engineer, Technical Reviewer.
**Skills.** Cat 5 (Part 5), 14, 21, 22, 23.

### Tasks

| ID | Task and objective | How to execute | Outputs | Validation |
|---|---|---|---|---|
| P03-T01 | **User research, information architecture.** | Use the personas from P01. Without real users, label output "hypotheses" and plan validation. Build the sitemap, navigation model, content model, and permission-aware IA (what each role sees). | Persona set, IA map | Each persona goal maps to a path in the IA. |
| P03-T02 | **User flows, wireframes, prototypes.** | Diagram flows incl. error, empty, offline, unauthorized, and timeout paths. Produce low-fi wireframes, then a clickable prototype for critical flows. Run a heuristic review (Nielsen) and usability testing if users are available. | Flow diagrams, wireframes, prototype | Every acceptance criterion in P01 has a screen and state. |
| P03-T03 | **Design system and accessibility baseline.** | Define design tokens (color, type, spacing), components with states, responsive breakpoints (mobile-first), and content guidelines. Accessibility to **WCAG 2.2 AA**: contrast, focus order, keyboard operability, semantic HTML first and ARIA only when needed, labels, error association, motion preferences, and target size. | Design System Spec, Accessibility Spec | Automated a11y checks pass. Manual keyboard and screen-reader check done on key flows. |
| P03-T04 | **Frontend architecture and scaffolding.** | Choose the rendering model by need (SPA, SSR/SSG, or hybrid, with SEO and performance as drivers). Define the folder structure by feature, typed API client generated from the contract, routing with route guards (UX only, never security), state strategy (server state via a cache library, local UI state local, global state minimized), error boundaries, and environment config (no secrets). | Frontend scaffold, ADR | Build is reproducible. Lint, type-check, and format gates are enforced in CI. |
| P03-T05 | **Component-driven implementation.** | Build the components in isolation (component workbench), with props typed, states complete (default, hover, focus, disabled, loading, error, empty), and tests per component. Prefer composition. Keep presentational and data-fetching components separate. | Component library, stories, tests | Each component has a11y and interaction tests. |
| P03-T06 | **Forms, validation, API integration, error and loading states.** | Client validation is for UX. **The server re-validates everything.** Handle API errors by mapping the error model to user messages that disclose no internals. Use optimistic UI only for safe, reversible actions. Debounce, cancel stale requests, and make retry idempotent. Use skeletons and timeouts. | Integrated screens | Contract tests against the mock server and the real API. All error codes are handled. |
| P03-T07 | **Frontend security hardening.** | Perform the controls below. | Security config, tests | Security checklist (§19.3) complete. |
| P03-T08 | **Performance and compatibility.** | Set budgets (for example Core Web Vitals targets: LCP, INP, CLS) from NFRs. Use code splitting, lazy loading, image optimization, caching headers, and bundle analysis. Define the supported browser matrix from analytics or requirements, and test it. Use progressive enhancement. | Performance report, compat matrix | Budgets are met in CI. Compat tests are green on the matrix. |
| P03-T09 | **Frontend verification and handoff.** | Run the full frontend test suite. Produce documentation. Create the handoff packet (§8.8). | Verified frontend plus docs | Gate G5 for each change. Part of G6. |

**Frontend security controls (P03-T07)**

| Threat | Control (required) | Verification |
|---|---|---|
| XSS | Use framework auto-escaping. Forbid raw HTML injection APIs (`innerHTML`, `dangerouslySetInnerHTML`, and so on) unless sanitized with a vetted sanitizer (for example DOMPurify) and reviewed. Context-aware output encoding. Trusted Types where supported. | SAST rule, review, and XSS payload tests |
| XSS impact reduction | **CSP**: nonce- or hash-based `script-src`, `object-src 'none'`, `base-uri 'none'`, `frame-ancestors`. Roll out first in Report-Only, then enforce. Avoid `unsafe-inline` and `unsafe-eval`. | CSP evaluator and browser test |
| CSRF | For cookie-based sessions: `SameSite` (Lax/Strict), anti-CSRF tokens (synchronizer or signed double-submit) on state-changing requests, and Origin/Fetch-Metadata validation on the server. | Negative CSRF tests |
| Session handling | Cookies `HttpOnly; Secure; SameSite`. Prefer server-managed sessions or a BFF pattern over tokens in `localStorage` (which is exposed to XSS). Logout invalidates server-side. | Cookie attribute test |
| Auth flows | Authorization Code flow with PKCE. No implicit flow. Validate `state` and `nonce`. No credentials in URLs. Generic login errors. Account recovery that does not enumerate accounts. | Flow tests |
| Clickjacking | `frame-ancestors` CSP (and `X-Frame-Options` as legacy). | Header check |
| Sensitive data exposure | No secrets, API keys with privilege, or sensitive PII in bundles, source maps in production, local/session storage, URLs, analytics, or error trackers. Mask on display. `Cache-Control: no-store` for sensitive pages. | Bundle secret scan, header review |
| Third-party scripts and dependencies | Minimize them. Subresource Integrity (SRI) for CDN assets. Lockfiles. SCA scan. Review install scripts. | SCA report |
| Client-side limits | The client is untrusted. Hiding a button or guarding a route is **UX, not authorization**. | Server-side authZ tests exist for each action |
| Other | `Referrer-Policy`, `Permissions-Policy`, `X-Content-Type-Options: nosniff`, safe handling of `postMessage` (check origin), safe URL handling (allowlist schemes), and `rel="noopener"`. | Header and review checks |

**Validation and acceptance.** All screens in the prototype are implemented and match the design spec. a11y: 0 critical or serious automated violations, and manual checks passed on key flows. Performance budgets met. CSP is enforced with no violations in the standard flows. SAST and SCA show 0 unresolved High/Critical.
**Deliverable.** Implemented and tested frontend with documented design specifications.
**Failure handling.** If a design requires an insecure pattern (for example a token in `localStorage` for convenience), escalate to the Architect with an alternative. Do not implement it silently.
**Transition.** Handoff to QA (P07) and the Security Engineer (P06). Integration with P04 through the contract.

---
