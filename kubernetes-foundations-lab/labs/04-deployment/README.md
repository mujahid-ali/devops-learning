# Lab 04 — Deployment, ReplicaSet and rolling update

## Goal

Use a controller to declare two replicas and watch Kubernetes maintain that desired state.

## Create the Deployment

The naked Pod should be gone from Lab 03. Apply only this object:

```sh
kubectl apply -f manifests/02-deployment/web-deployment.yaml
kubectl get deployment,replicaset,pod -n playground -o wide
kubectl rollout status deployment/web -n playground
```

Read the Deployment selector and Pod-template labels. They must agree. Then delete one Deployment-managed Pod and watch its ReplicaSet create a replacement:

```sh
kubectl delete pod -n playground -l app=web
kubectl get pods -n playground --watch
```

## Rolling update

Change the image tag in `manifests/02-deployment/web-deployment.yaml` to another valid NGINX tag, then apply it and inspect:

```sh
kubectl apply -f manifests/02-deployment/web-deployment.yaml
kubectl rollout status deployment/web -n playground
kubectl rollout history deployment/web -n playground
```

Rollback after you have seen the old/new ReplicaSets:

```sh
kubectl rollout undo deployment/web -n playground
```

## Questions

- Why is deleting a Pod a poor deployment strategy?
- What does the Deployment own directly, and what does the ReplicaSet own?
- Why do readiness probes matter during a rolling update?

## Done when

Two ready Pods exist, a deleted Pod is replaced, and you have performed and explained one rollback.
