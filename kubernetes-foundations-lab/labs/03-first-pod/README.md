# Lab 03 — Your first Pod

## Goal

Create the smallest useful workload and observe its complete lifecycle.

## Apply one object at a time

Do **not** run `kubectl apply -k manifests`; that file exists only for local YAML rendering. Apply these two files deliberately:

```sh
kubectl apply -f manifests/00-namespace/namespace.yaml
kubectl apply -f manifests/01-pod/web-pod.yaml
```

Observe it:

```sh
kubectl get pod -n playground -o wide
kubectl describe pod web-pod -n playground
kubectl logs web-pod -n playground
kubectl exec -n playground web-pod -- nginx -v
```

Use `kubectl port-forward -n playground pod/web-pod 8080:80`, leave it running in one terminal, and request `http://localhost:8080` from another.

## Trace the lifecycle

Use the Pod’s `NODE` column and its events to answer:

1. Who chose the node?
2. What image was pulled?
3. Which node’s kubelet asked the runtime to start it?
4. Why does port-forward work without a Service or external load balancer?

## Break/fix — A naked Pod is not self-healing

Delete only this Pod:

```sh
kubectl delete pod web-pod -n playground
kubectl get pods -n playground --watch
```

No replacement will appear. This is the reason for the next lab: a Pod is a unit of execution, not a desired replica count.

## Done when

You can contrast a running container, a Pod and a Kubernetes node, and can explain why the deleted Pod remains absent.
