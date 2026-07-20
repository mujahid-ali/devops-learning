# Lab 02 — See the control plane and workers

## Goal

Inspect the components that were created in Lab 01 and map them to the mental model.

## Inspect through the API

```sh
kubectl get nodes -o wide
kubectl get pods -n kube-system -o wide
kubectl get --raw=/readyz
kubectl get daemonsets -n kube-system
kubectl get deployments -n kube-system
```

Find CoreDNS, kube-proxy and the CNI/kindnet components. Identify which components run one-per-node and which have a separate replica model.

## Inspect the control-plane node

The following commands run *inside the local Docker node container*, not on macOS:

```sh
docker exec k8s-foundations-control-plane ls -1 /etc/kubernetes/manifests
docker exec k8s-foundations-control-plane crictl ps -a
docker exec k8s-foundations-control-plane ps aux
```

The static-Pod manifests in `/etc/kubernetes/manifests` explain why the API server, etcd, scheduler and controller manager exist even though you did not apply their YAML with `kubectl`.

## Inspect a worker

```sh
docker exec k8s-foundations-worker crictl ps -a
docker exec k8s-foundations-worker ls -la /etc/cni/net.d
kubectl describe node k8s-foundations-worker
```

## Questions to answer in your notes

1. Which component reads static Pod files on the control-plane node?
2. Which component selects a node for a newly created Pod?
3. Which component starts the selected Pod’s container?
4. How are Services different from CoreDNS?
5. What changes if a worker node becomes `NotReady`?

## Done when

You can point to a command output for each component in the [mental model](../../docs/00-kubernetes-mental-model.md), rather than relying on a diagram alone.
