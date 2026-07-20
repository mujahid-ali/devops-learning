# How this local Kubernetes cluster is created

## The exact creation action

In Lab 01 you will run:

```sh
kind create cluster --name k8s-foundations --config kind/cluster.yaml --wait 60s
```

`kind` reads `kind/cluster.yaml` and uses the Docker engine to create three Linux containers:

```text
k8s-foundations-control-plane     control-plane node
k8s-foundations-worker            worker node; maps localhost:8080 → NodePort 30080
k8s-foundations-worker2           worker node
```

They are not ordinary application containers: each container acts as a Kubernetes node and includes a container runtime, kubelet and node tooling. kind bootstraps the control-plane node, writes a kubeconfig on your machine, joins the workers, and waits for the API server to be ready.

## What happens after `kubectl apply`

For a Pod manifest, this is the shortest accurate story:

1. `kubectl` sends the manifest to the API server.
2. The API server validates it and stores desired state in etcd.
3. The scheduler chooses a worker for the pending Pod.
4. That worker’s kubelet observes the assignment.
5. The kubelet asks containerd to pull the image and create the Pod’s containers.
6. The CNI plugin configures network connectivity. The kubelet reports status back to the API server.

Use the commands in Lab 02 to see components from steps 1–6 rather than memorising this list.

## Why not bootstrap with `kubeadm` first?

`kubeadm` is an excellent next layer, especially on your disposable VMs. It requires you to manage operating-system prerequisites, package versions, cgroups, swap, a container runtime, node networking, certificates and join tokens. Start it only after this repository’s flow is familiar; otherwise failures will be hard to classify.

When ready, recreate this same topology on three disposable Linux VMs:

1. Prepare the operating system and container runtime on all nodes.
2. Run `kubeadm init` only on the control-plane VM.
3. Install one CNI plugin and wait for CoreDNS to become ready.
4. Join each worker with the generated command.
5. Repeat Labs 02–07 unchanged. Compare what kubeadm exposes with what kind supplied automatically.

Do this only on dedicated VMs, never on an existing machine that runs important workloads.
