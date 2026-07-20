# ForgePaaS architecture

## Purpose

ForgePaaS is a small internal platform for registering an application’s desired state and, in later labs, reconciling it into Kubernetes. It is intentionally small enough to understand end to end and rich enough to demonstrate staff-level trade-offs: isolation, delivery, operability, safe rollout, failure handling, and cloud portability.

## Architecture boundaries

| Boundary | Stage 1: local learning implementation | Later extension |
|---|---|---|
| Developer interface | FastAPI REST API; curl and test client | Python CLI, authentication, audit log |
| Desired state | Thread-safe in-memory store | PostgreSQL migrations and transaction semantics |
| Asynchronous work | None yet | Redis-backed work queue and idempotent reconciliation jobs |
| Workload runtime | Static baseline Kubernetes manifests | Control plane generates/reconciles Deployment, Service, ConfigMap, Secret, HPA and NetworkPolicy |
| Delivery | GitHub Actions verifies tests and builds images | registry publishing, image scan, release promotion and rollback |
| Ingress | ClusterIP services plus port-forward | ingress controller, TLS, DNS and rate limits |
| Telemetry | Prometheus-format `/metrics`; container logs | Prometheus, Grafana, Loki, alert rules and SLO dashboards |
| Infrastructure | Docker Desktop + kind, RHEL-compatible practice VMs | Terraform-managed AWS VPC, IAM, ECR, EKS, S3 state, ALB |

## Main data flows

### Present baseline

1. A developer submits an `ApplicationSpec` to `POST /api/v1/apps`.
2. The control plane validates the name, image, replica count and port, then keeps the desired state in process memory.
3. The control plane publishes structured application logs and a Prometheus counter.
4. `echo-service` is independently deployed on kind as a known tenant workload. It provides health endpoints and a metrics endpoint for operations exercises.

The present API **does not claim to deploy workloads**. That honesty makes the persistence/reconciliation labs real engineering work instead of a misleading demo.

### Target flow

1. A repository push triggers GitHub Actions to test, build and scan an image.
2. CI publishes an immutable image tag to a local registry in Stage 1 or ECR in Stage 2.
3. A developer registers a versioned application spec with the control plane.
4. The reconciler validates policy, persists the change, and creates or patches Kubernetes resources.
5. Kubernetes rolls out the workload; probes, HPA, ingress, metrics and logs reveal its health.
6. An unsafe rollout is halted or rolled back using a recorded runbook.

## Design decisions already made

- Python/FastAPI is the control-plane language because Python automation, REST APIs, CLI design, logging, testing, subprocess work, SSH, JSON/YAML and concurrency are explicit learning objectives.
- PostgreSQL is the durable desired-state store; Redis is reserved for cache and worker-queue exercises. Starting with in-memory state makes their value observable.
- Docker Desktop and kind keep the first stage reproducible and cost-free. Disposable RHEL-compatible VMs handle SELinux, systemd, LVM, RAID and SSH exercises that containers cannot teach safely.
- Kubernetes manifests use Kustomize first. Helm is introduced later so its templating/packaging trade-off is understood rather than hidden.
- AWS is a portability stage, not a prerequisite. Terraform modules will translate stable local contracts into IAM, VPC, ECR, EKS, S3 remote state and ALB resources.

See [ADR 0001](adr/0001-local-first.md) for the local-first decision and [the AWS boundary](../infra/stage-2-aws/README.md) for what is deferred.
