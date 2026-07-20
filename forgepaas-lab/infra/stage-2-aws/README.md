# Stage 2 AWS boundary

Do not apply this stage until the local project has completed the baseline delivery, Kubernetes and observability labs. This directory is intentionally documentation-only today: it prevents accidental cost while defining the target infrastructure contract.

## Terraform module plan

```text
bootstrap/        one-time S3 remote state and state-lock configuration
modules/
  network/        VPC, public/private subnets, route tables, NAT and VPC endpoints
  identity/       least-privilege IAM roles and policies
  registry/       ECR repositories and lifecycle policies
  platform/       EKS cluster, managed node groups and access entries
  edge/           ALB, target groups, ACM/TLS and security groups
  observability/  CloudWatch integration and platform alert destinations
environments/dev/ composition, variables, outputs and remote-state wiring
```

## Required acceptance criteria

- `terraform fmt`, `validate` and `plan` run without applying resources.
- State is remote in S3 and protected against concurrent modification. No state file or credential is committed.
- IAM grants only the actions required by the deployment path; human administrator credentials are not used by CI.
- VPC routing, NAT, security groups and ALB health checks are diagrammed and tested from an external client and a private workload.
- ECR accepts immutable deployment images; EKS deploys the same Helm chart used locally.
- A failed rollout has a tested rollback procedure and a documented cost-destruction procedure.

## Deliberate AWS topic coverage

| Playbook topic | Project evidence |
|---|---|
| IAM | role trust policies, least-privilege Terraform and CI identity design |
| VPC / routing / NAT | module, diagram, reachability tests and a broken-route incident |
| EC2 | a temporary troubleshooting host or self-managed runner comparison |
| ECR | image repository, lifecycle policy and immutable tag policy |
| EKS concepts | managed control plane, nodes, add-ons, access and upgrade trade-offs |
| S3 | Terraform remote state and an object-storage system-design exercise |
| CloudWatch | control-plane and EKS log/metric export comparison with Grafana/Loki |
| Security Groups / ALB | allow-list policy, health check, TLS and ingress failure exercise |
| Terraform basics | providers, resources, variables, modules, state, plan/apply and outputs |

Before implementation, add `terraform/` source here and review its plan before every apply.
