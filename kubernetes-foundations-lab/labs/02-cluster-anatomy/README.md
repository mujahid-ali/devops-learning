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

1. Which component reads static Pod files on the control-plane node? A: kubectl
2. Which component selects a node for a newly created Pod? A: kube-scheduler
3. Which component starts the selected Pod’s container?A: continer run time (containerd or CRI-O) starts the pod's container, kubelet watches the api-server and notices a pod has been assigned to it's node, the kubelet send an instrution to container runtime using the Container Runtime Interface (CRI) protocol.: The container runtime pulls the required container image (if not already cached) and interacts with the host operating system kernels to start the container namespaces and processes.
4. How are Services different from CoreDNS?
A: While both manage communication inside a cluster, Services are abstract network routing rules, whereas CoreDNS is the software that translates human-readable names into those routing rules.
A Service is a Routing Rule: It provides a single, permanent IP address (ClusterIP) and port that points to a group of moving Pods. It is an internal load balancer managed by kube-proxy.
CoreDNS is a Name Translator: It is a cluster-wide application that resolves DNS queries. When a Pod tries to talk to my-service, CoreDNS translates that text name into the Service's ClusterIP.

How They Work Together:When Pod A wants to send data to Pod B using a Service named backend:Pod A asks CoreDNS: "What is the IP for backend?"CoreDNS replies: "The IP is 10.96.0.10."Pod A sends traffic to 10.96.0.10.The Service (kube-proxy) intercepts that traffic and forwards it to the actual target Pod.

5. What changes if a worker node becomes `NotReady`?
A:
When a worker node changes to a NotReady status, the Kubernetes control plane activates a multi-stage safeguard pipeline to isolate the unhealthy node and protect the rest of the cluster.The sequence of automated changes unfolds in the following order:1. The Node Is Tainted (Immediate)The node controller immediately applies a node.kubernetes.io/not-ready taint to the affected Node object.The effect: The taint uses the NoSchedule effect. The kube-scheduler immediately stops placing any newly created Pods onto this node.2. Traffic Routing Stops (Within Seconds)To prevent network requests from hitting a dead or unresponsive environment, the cluster adjusts its routing:Endpoint Elimination: The Endpoints Controller removes all Pods running on the NotReady node from any active Service Endpoint slices.
Kube-proxy Action: Local kube-proxy agents on the other healthy nodes update their iptables or IPVS rules to stop sending network traffic to the affected node's Pods.3. Automatic Pod Eviction (After a Timeout)The existing Pods running on that node are not destroyed immediately, allowing a grace period in case the node simply suffered a brief network blip.The Countdown: By default, Kubernetes automatically injects a toleration of 300 seconds (5 minutes) onto your Pods for the NotReady taint.The Eviction: If the node remains NotReady after 5 minutes, the kube-controller-manager initiates a Taint-based Eviction. The control plane sets the Pod statuses on that node to Terminating.4. Workload ReschedulingHow the workloads recover depends entirely on how they were deployed:Deployments / ReplicaSets: The control plane realizes the cluster has dropped
below its desired replica count. The kube-scheduler selects alternative, healthy nodes to spin up brand-new replacement Pods.Bare Pods: A standalone Pod (created without a controller) is bound directly to that specific node. It will not be recreated elsewhere and will remain unhelpful.DaemonSets: Because DaemonSets are designed to run exactly one Pod per node, those Pods are not rescheduled to other nodes.⚠️ Important Caveat: The "Terminating" StateIf the worker node lost total network connectivity or lost power entirely, the control plane cannot communicate with the local kubelet to confirm the physical destruction of the old containers. As a result, the old Pods on the NotReady node will remain visibly stuck in a Terminating state indefinitely until the node recovers or is manually deleted.
## Done when

You can point to a command output for each component in the [mental model](../../docs/00-kubernetes-mental-model.md), rather than relying on a diagram alone.
