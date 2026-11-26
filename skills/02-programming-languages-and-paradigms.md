### 2. Programming Languages and Paradigms

| Skill | Description and knowledge | Practical competencies | Tools | Applied in | Level | Validation |
|---|---|---|---|---|---|---|
| Primary-language mastery (per project) | Language semantics, type system, standard library, error and concurrency model, and the idioms and security pitfalls of that language | Write idiomatic, typed, tested code. Know the dangerous APIs (unsafe deserialization, eval, reflection, native interop). | The language toolchain, linters, formatters, type-checkers | P03–P05 | M, L4 for the project's main language | CR, TC |
| Paradigm fluency (OO, functional, procedural, and async or reactive) | Trade-offs, immutability, side-effect isolation, and the async pitfalls (blocking, cancellation, and backpressure) | Choose and apply the paradigm to the problem. | n/a | P04 | M, L3 | CR |
| Secondary languages (SQL, shell, and configuration languages such as YAML and HCL) | Correct and safe use. Quoting pitfalls, injection, and idempotency | Write safe SQL and shell scripts (strict mode, quoting). | psql/CLI, shellcheck | P05, P08 | M, L3 (SQL L4 for DB role) | LAB |
| Scripting for automation and security tooling | Rapid tools for parsing, glue, and test harnesses | Automate repeated tasks with tests and error handling. | Python, Bash, or similar | P06, P08 | S, L3 (R: Security, DevOps) | LAB |
| Memory-unsafe languages (C and C++), if the project uses them | Buffer, integer, and lifetime vulnerabilities, sanitizers, and fuzzing | Write and review code using safe patterns | ASan, UBSan, fuzzers | Where used | S, L4 | CR, SEED |
