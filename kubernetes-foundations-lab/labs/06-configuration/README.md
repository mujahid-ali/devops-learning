# Lab 06 — ConfigMap, Secret and a safe configuration change

## Goal

Separate content/configuration from an image and understand what a Secret does—and does not—protect.

## Apply configuration objects

```sh
kubectl apply -f manifests/04-configuration/web-config.yaml
kubectl get configmap,secret -n playground
kubectl describe configmap web-content -n playground
```

Inspect the Secret metadata only. If you view its YAML, notice that its `data` is base64-encoded; base64 is **not encryption**. The training value is fake. Never run this exercise with a real secret in Git.

## Consume the ConfigMap

Edit `manifests/02-deployment/web-deployment.yaml` yourself. Under the NGINX container, add a `volumeMounts` entry mounting a `web-content` volume at `/usr/share/nginx/html`. Under the Pod spec, add a `volumes` entry referencing the `web-content` ConfigMap.

Apply the changed Deployment and watch the rollout:

```sh
kubectl apply -f manifests/02-deployment/web-deployment.yaml
kubectl rollout status deployment/web -n playground
curl -s http://localhost:8080
```

Read your rendered Pod specification with `kubectl get pod -n playground -l app=web -o yaml` and identify the volume mount.

## Questions

1. Why should an image not contain environment-specific page content or credentials?
2. Why does a ConfigMap update not necessarily produce an instant application reload?
3. What stronger controls would a production Secret need (encryption at rest, RBAC, external secret manager, rotation)?

## Done when

The browser shows your ConfigMap content and you can identify the difference between a ConfigMap, a Secret, a volume, and an environment variable.
