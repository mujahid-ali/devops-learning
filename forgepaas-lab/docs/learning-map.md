# Complete learning map

This is the traceability map from the career playbook to project evidence. A topic is complete only when its lab has a baseline, a fault, a repair, automated or repeatable validation, and a short incident note.

| Programme area | Where it is exercised | Evidence produced |
|---|---|---|
| Linux: processes, scheduling, signals, systemd, memory, filesystems, LVM, RAID, SELinux, cgroups, namespaces, performance, SSH, packages and troubleshooting | [Lab 01](../labs/01-linux/README.md) on disposable RHEL-compatible VMs and containers | commands, metrics before/after, service unit, storage and SELinux repair notes |
| Networking: OSI/TCP-IP, DNS, routing, NAT, HTTP/HTTPS, TLS, load balancing, reverse proxy, VPN, nftables, packets and Kubernetes networking | [Lab 02](../labs/02-networking/README.md) and [Lab 05](../labs/05-kubernetes/README.md) | packet capture, route/firewall rules, TLS diagnosis and network-policy tests |
| Python: automation, REST, CLI, concurrency, logging, tests, packaging, subprocess, SSH, JSON/YAML | [Lab 03](../labs/03-python-control-plane/README.md) | tested control-plane commits and a diagnostic CLI |
| Docker, Kubernetes and system design fundamentals | [Labs 04–05](../labs/README.md) | Dockerfiles, images, manifests, policies, ADRs and failure analysis |
| CI/CD, builds, logging, monitoring, HA and distributed locking | [Labs 06–08](../labs/README.md) | pipeline, release/rollback record, dashboards, alerts and reliability design |
| AWS and Terraform | [Stage 2 boundary](../infra/stage-2-aws/README.md) | reviewed Terraform plan, network diagram and deployed dev environment |
| Ten named system-design prompts | [System-design tracker](../practice/system-design/README.md) | one timed design packet per prompt |
| 180 medium-focused DSA problems | [DSA tracker](../practice/dsa/README.md) | tested solutions and retrospective notes |
| STAR stories, resume, LinkedIn, applications and mocks | [Career tracker](../practice/career/README.md) | quantified stories, portfolio README and application/mocks log |

The [lab index](../labs/README.md) provides the ordered hands-on path; the practice trackers prevent interview work from being forgotten while the platform is built.
