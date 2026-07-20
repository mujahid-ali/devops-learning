# Lab 03 — Python automation and the control plane

The baseline API is in `control-plane/app/main.py`. Improve it in small, tested commits; do not jump directly to a framework-heavy implementation.

| Exercise | Playbook coverage | Deliverable |
|---|---|---|
| 03.1 API contract | REST APIs, JSON and validation | versioned request/response schema and negative tests |
| 03.2 Operator CLI | CLI, packaging and JSON/YAML | `forgepaasctl` command to register/list applications from YAML |
| 03.3 Durable state | PostgreSQL, transactions and migration | persistence layer and a restart-survival test |
| 03.4 Cache/work queue | Redis, concurrency and idempotency | asynchronous reconcile job with duplicate-request protection |
| 03.5 Diagnostic runner | subprocess and logging | safely capture `kubectl` diagnostics with timeout, redaction and exit-code handling |
| 03.6 Remote probe | SSH automation | key-based VM health probe with host-key verification and structured output |
| 03.7 Test quality | testing and packaging | unit, API, failure-path and integration tests run in CI |

## Break/fix 03.1 — A duplicate application is created under concurrency

**Inject:** Send the same registration request concurrently from several clients after persistence is introduced.

**Investigate:** Observe the race in logs/database state. Define the idempotency key and database uniqueness constraint.

**Repair:** Make duplicate submissions return a deterministic result without duplicate workloads or queue jobs.

## Break/fix 03.2 — A diagnostic subprocess hangs

**Inject:** Call a command that does not exit from the diagnostic runner.

**Investigate:** Distinguish command timeout, child-process cleanup, stdout/stderr capture and shell-injection risks.

**Repair:** Use argument arrays, explicit timeout, bounded output, process cleanup and useful structured error logs.
