# Lab 08 — Reliability and distributed systems

This lab turns the control plane into a staff-level system-design and implementation exercise. State the required consistency and recovery semantics before adding infrastructure.

| Scenario | Concepts to apply |
|---|---|
| Duplicate deploy event | queue delivery, idempotency, transactions and distributed locking |
| Stale application read | caching, invalidation and consistency budget |
| Reconciler crash mid-deploy | retry/backoff, desired versus observed state, durable events and rollback |
| PostgreSQL primary unavailable | replication, failover, RPO/RTO, backups and client reconnect behavior |
| Hot tenant | partitioning/sharding criteria, rate limits, priority queues and HPA |
| Control plane availability | HA deployment, leader election/locking, health checks and split-brain avoidance |

## Break/fix 08.1 — Two workers deploy the same spec

Run two reconciliation workers against the same queued request. Demonstrate the duplicate side effect, then use an idempotency key and a scoped lock/transactional claim. Explain why the lock alone is not enough if it can expire.

## Break/fix 08.2 — Cache returns a deleted application

Introduce a cache-aside read with no invalidation. Reproduce the stale read, choose a consistency target, repair invalidation/versioning, and document the remaining failure window.
