# Kubernetes mental model

Kubernetes is a system for continuously moving **actual state** toward a declared **desired state**.

```text
you (kubectl + YAML)
        |
        v
API server <-> etcd (cluster state)
   |                 |
   |                 +-> controllers notice desired/actual differences
   v
scheduler selects a worker node
   |
   v
kubelet asks containerd to run the Pod
   |
   v
CNI gives the Pod networking; kube-proxy/service rules direct traffic
```

## The components you must recognise

| Component | Runs where | Purpose |
|---|---|---|
| `kubectl` | your machine | authenticated API client; it does not create containers directly |
| kube-apiserver | control-plane node | the cluster’s API front door; validates and persists requests |
| etcd | control-plane node | consistent key-value store for Kubernetes state |
| kube-scheduler | control-plane node | chooses a suitable node for unscheduled Pods |
| kube-controller-manager | control-plane node | controllers compare desired state with actual state and make corrections |
| kubelet | every node | watches assigned Pods and asks the runtime to run them |
| containerd | every node | container runtime that pulls images and runs containers |
| kube-proxy | every node | implements Service traffic rules |
| CNI / kindnet | every node | gives Pods network interfaces and routes |
| CoreDNS | cluster workload | lets workloads resolve Service names |

## Object progression in this lab

1. **Namespace** gives our learning resources a boundary.
2. **Pod** shows the smallest deployable unit and why it is not self-healing by itself.
3. **Deployment** creates a ReplicaSet and continuously maintains a number of Pods.
4. **Service** supplies a stable virtual IP/DNS name for a changing set of Pods selected by labels.
5. **ConfigMap** and **Secret** separate configuration from an image.

Before issuing a command, ask: *Which component sees this object next, and what state change should it create?*
