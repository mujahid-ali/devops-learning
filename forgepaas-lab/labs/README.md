# Hands-on lab index

## Learning rule

For every exercise, write five lines before reading a solution: **symptom, evidence, hypothesis, repair, prevention**. Keep commands and sanitized output in `notes/` when a lab tells you to create it. A fault is not complete because a command happened to work; it is complete when you can explain why the fault occurred and prove that the repair holds.

## Ordered sequence

| Lab | Focus | Core break/fix outcomes |
|---|---|---|
| [00](00-workstation/README.md) | Workstation and evidence | Docker engine, kind, kube context, reproducibility and safe boundaries |
| [01](01-linux/README.md) | Linux and VM operations | process/service/memory/storage/SELinux/SSH failures on disposable VMs |
| [02](02-networking/README.md) | Networking and traffic | DNS, route, NAT, TLS, proxy, firewall, packet and Kubernetes network failures |
| [03](03-python-control-plane/README.md) | Python automation | API, CLI, tests, logs, JSON/YAML, subprocess/SSH and concurrency faults |
| [04](04-containers/README.md) | Docker and image engineering | broken build, bad entrypoint, permissions, networks, volumes and resource limits |
| [05](05-kubernetes/README.md) | Kubernetes primitives | workload, service, config, secret, RBAC, volume, stateful, daemon, HPA and policy faults |
| [06](06-delivery/README.md) | Build systems and CI/CD | failing test/build, supply chain, deployment, rolling update and rollback failures |
| [07](07-observability/README.md) | Metrics, logs and alerting | missing telemetry, bad dashboard/query, noisy alert and correlation exercises |
| [08](08-reliability/README.md) | Distributed-systems and resilience | cache, queue, consistency, replication, HA and distributed-locking scenarios |
| [09](09-system-design/README.md) | Staff-level design | timed designs and trade-off reviews based on the platform |

Finish a lab in order, but reserve one weekly session for DSA and another for a timed system-design packet. The tracker is in `practice/`.
