# ADR 0001: Start local, then move the same platform contracts to AWS

**Status:** Accepted

## Context

The learning plan requires Linux internals, Kubernetes, CI/CD, Terraform and AWS. Beginning in AWS would add cost, credentials, remote-network debugging and account policy concerns before the platform fundamentals are understood. Some core topics—SELinux, LVM, RAID, systemd, SSH and firewall troubleshooting—also need a real Linux VM rather than a container.

## Decision

Use Docker Desktop and kind for the runnable platform during Stage 1. Use the user’s disposable RHEL-compatible virtual machines for Linux, storage, SELinux, SSH and network labs. Do not create AWS resources until Stage 2.

Keep Kubernetes manifests, container interfaces, configuration, image names and observability endpoints portable so that Terraform can later introduce AWS without redesigning the application.

## Consequences

- Local feedback is fast and has no cloud cost.
- The early platform uses simulated or local equivalents for registry, load balancer, DNS and remote Terraform state.
- AWS-specific services still receive concrete design and acceptance criteria now, then an implementation in Stage 2.
- Every fault injection must identify whether it belongs in kind, Compose, or a disposable VM. It must never be run on the host machine.
