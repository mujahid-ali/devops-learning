# ForgePaaS Lab — Step 2

ForgePaaS Lab is a local-first, break/fix-oriented **Mini Platform as a Service**. It is the second project in this learning path: it grows from a Python monitoring/control-plane service into a Kubernetes platform with delivery automation, observability, reliability practices, and a later AWS/Terraform deployment.

> Prerequisite: first complete [Kubernetes Foundations Lab](../kubernetes-foundations-lab/README.md). That project explains how the local cluster is created and teaches core Kubernetes objects manually. ForgePaaS deliberately assumes those fundamentals so it can focus on platform engineering.

The project is deliberately not a collection of copy/paste deployments. Every module begins with a working baseline, introduces a realistic fault, and asks you to diagnose and repair it with evidence.

## Architecture

```text
developer -> GitHub Actions -> container registry -> control plane -> Kubernetes workloads
                                      |                  |                 |
                                      |                  |                 +-> ingress / TLS / HPA
                                      |                  +-> desired state API
                                      +-> test, build, scan                |
                                                                         metrics/logs
                                                                            |
                                                                  Prometheus / Grafana / Loki
```

The local Stage 1 platform runs in Docker Desktop and kind. Stage 2 keeps the same application and Kubernetes contracts but provisions AWS infrastructure with Terraform.

Read [the architecture](docs/architecture.md), then use [the lab index](labs/README.md) as your learning sequence.

## Repository layout

```text
control-plane/        Python FastAPI service and its tests
sample-apps/          a deployable tenant workload
k8s/                  local Kubernetes manifests (Kustomize)
infra/local/          kind configuration
infra/stage-2-aws/    AWS/Terraform design boundary; no cloud resources yet
labs/                 progressive hands-on and break/fix exercises
practice/             DSA, system-design and career-evidence trackers
docs/                 architecture decisions, runbooks and learning map
scripts/              repeatable local-platform actions
```

## First run

Docker Desktop must be running before any Docker, Compose, or kind command. Install kind once if it is not already installed; `kubectl` is already useful for inspecting the cluster.

```sh
cd /Users/mujahidali/Documents/devops-learning/forgepaas-lab
make help
make test
make up
curl http://localhost:8000/healthz
make kind-up
kubectl -n forgepaas get pods,svc
```

`make kind-up` builds the two local images, creates a `forgepaas` kind cluster if needed, loads the images into it, and applies the local manifests. It intentionally does not install anything or use AWS credentials.

For the first learning session, begin with [Lab 00](labs/00-workstation/README.md), then complete the first two Linux exercises in [Lab 01](labs/01-linux/README.md).

## Safety boundary

- Never commit real cloud credentials, kubeconfigs, private keys, or `.env` files.
- Run destructive storage, SELinux, firewall, and routing exercises only on your disposable VMs—not on your daily machine.
- Keep a short incident note for each break/fix: symptom, evidence, hypothesis, repair, and prevention.

## What is already implemented

- A containerized FastAPI control plane with health, readiness, Prometheus metrics, and desired-state registration endpoints.
- A lightweight tenant `echo-service` with health endpoints and Prometheus-format metrics.
- Docker Compose for the local control-plane dependencies (PostgreSQL and Redis).
- Local kind cluster configuration, Kubernetes Deployments/Services, and a safe bootstrap script.
- A complete learning map and staged fault-injection exercise catalogue.

Cloud infrastructure, GitHub Actions, Helm packaging, ingress/TLS, central logging, and persistence are intentionally staged after their foundations have been learned. Their acceptance criteria are already captured in the lab sequence so the project grows without architecture drift.
