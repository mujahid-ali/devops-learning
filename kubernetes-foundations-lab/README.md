# Kubernetes Foundations Lab — Step 1

This is the project to complete **before** ForgePaaS. It has no application code and no automation that hides Kubernetes from you. You first create a local cluster yourself, inspect the containers that form its nodes, then add one Kubernetes object at a time.

The outcome is not merely “I can run `kubectl apply`.” You will be able to explain:

- what creates a local kind cluster;
- which control-plane and worker components make it work;
- how a Pod becomes a running container on a node;
- how labels, Deployments, Services, DNS, configuration and probes connect; and
- how to collect evidence when a workload fails.

## Learning path

```text
Step 1 — this repository
Docker engine → kind node containers → control plane → Pods → Deployments
→ Services/DNS → ConfigMaps/Secrets → failure diagnosis

Step 2 — ../forgepaas-lab
Python control plane → CI/CD → Helm/Ingress → observability → reliability → AWS/Terraform
```

## What “from scratch” means here

You will manually run `kind create cluster` and inspect every resulting node and system component. `kind` is a learning-friendly bootstrapper: it creates Docker containers that act as Linux Kubernetes nodes, then bootstraps Kubernetes inside them. It is not the same as enabling Docker Desktop’s managed Kubernetes checkbox.

Building Kubernetes binaries, certificates and an etcd cluster entirely by hand is a valuable but much later exercise. It would obscure the fundamentals you need first. An optional VM/kubeadm extension is described in [the cluster-creation guide](docs/01-how-kind-creates-a-cluster.md).

## Prerequisites

1. Docker Desktop running—not merely installed.
2. `kubectl` installed.
3. `kind` installed. On macOS with Homebrew: `brew install kind`.

Verify all three before moving on:

```sh
docker info
kubectl version --client
kind version
```

## Start here

Follow the labs in order. Do not skip directly to manifests.

1. [Lab 00 — prerequisites](labs/00-prerequisites/README.md)
2. [Lab 01 — create the cluster yourself](labs/01-create-cluster/README.md)
3. [Lab 02 — inspect how the cluster works](labs/02-cluster-anatomy/README.md)
4. [Lab 03 — first Pod](labs/03-first-pod/README.md)
5. [Lab 04 — Deployment](labs/04-deployment/README.md)
6. [Lab 05 — Service and networking](labs/05-service-networking/README.md)
7. [Lab 06 — configuration](labs/06-configuration/README.md)
8. [Lab 07 — troubleshooting](labs/07-troubleshooting/README.md)
9. [Lab 08 — move to Step 2](labs/08-next-step/README.md)

Keep a small `notes/` folder locally (do not commit credentials) with five items for each lab: **symptom, evidence, hypothesis, repair, prevention**.

## Safety

- This lab creates only a local, disposable cluster named `k8s-foundations` in Docker Desktop.
- It creates no cloud resources and needs no AWS credentials.
- Delete only this lab’s cluster when you are done:

  ```sh
  kind delete cluster --name k8s-foundations
  ```

- The Secret exercise uses an obviously fake value. Never put a real token or password in a manifest or Git repository.
