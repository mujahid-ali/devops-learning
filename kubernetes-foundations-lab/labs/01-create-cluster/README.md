# Lab 01 — Create the cluster yourself

## Goal

Create a three-node Kubernetes cluster without a helper script, then prove which local containers are its nodes.

## Read first

Read [how kind creates a cluster](../../docs/01-how-kind-creates-a-cluster.md). Then read every line of [`kind/cluster.yaml`](../../kind/cluster.yaml). It defines one control-plane node and two worker nodes; it is not a workload manifest.

## Create it

From the repository root, run exactly:

```sh
kind create cluster --name k8s-foundations --config kind/cluster.yaml --wait 60s
```

Then confirm your current context and API server:

```sh
kubectl config current-context
kubectl cluster-info
kubectl get nodes -o wide
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}'
```

You should find `k8s-foundations-control-plane`, `k8s-foundations-worker`, and `k8s-foundations-worker2` in Docker. `kubectl get nodes` shows the same logical machines through the Kubernetes API.

## Important question

Why does `kubectl get nodes` still work even though you did not point it at an IP address? Find the generated `kind-k8s-foundations` context in `kubectl config view` and identify its server address and certificate reference. Do not paste the full kubeconfig into notes or a public repository.

## Clean reset

If you need to start over, use only this lab’s cluster name:

```sh
kind delete cluster --name k8s-foundations
```

Then recreate it using the same manual command. A clean reset is often the fastest way to test whether your instructions are complete.

## Done when

- You can draw the host → Docker → node-container relationship.
- You can explain why three node containers do not mean three control planes.
- You can identify the kubeconfig context used by `kubectl`.
