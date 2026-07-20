# Lab 00 — Prerequisites and the command boundary

## Goal

Know what is local tooling, what is a cluster component, and what each tool is allowed to do before creating a cluster.

## Do this manually

```sh
docker info
docker version
kubectl version --client
kind version
kubectl config get-contexts
```

## Explain the result

| Tool | Role | Does it create Kubernetes workloads directly? |
|---|---|---|
| Docker Desktop | local container engine used by kind | no; kind asks Docker to create node containers |
| kind | creates disposable Kubernetes node containers and bootstraps Kubernetes | only during cluster creation |
| kubectl | API client configured with a cluster context | no; it asks the API server to record desired state |
| kubelet | node agent inside each cluster node | yes, indirectly: it asks the container runtime to run Pods assigned to its node |

## Break/fix — Docker installed but unavailable

Quit Docker Desktop or run this lab before its engine is ready, then execute `docker info`.

Record the difference between a missing CLI and a running client that cannot reach its daemon. Start Docker Desktop, wait for it to report it is running, then repeat the command. Do not move on until this is clear.

## Done when

- You can state which command creates the cluster and which command applies desired state.
- Docker’s engine, `kubectl`, and `kind` all return version/health information.
- You have confirmed that no existing Kubernetes context is about to be changed accidentally.
