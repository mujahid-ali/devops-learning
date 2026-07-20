# Lab 05 — Kubernetes as a platform substrate

Start from `make kind-up`. Inspect the rendered manifests with `kubectl kustomize k8s/overlays/local` before applying anything.

| Exercise | Topics and platform extension |
|---|---|
| 05.1 Workloads | Pods, Deployments, rollout history and rollback using the echo service |
| 05.2 Discovery | Services, EndpointSlices, selectors and in-cluster DNS |
| 05.3 Configuration | ConfigMaps, Secrets, environment/volume consumption and safe secret handling |
| 05.4 Persistent apps | volumes, PVCs, StatefulSet and ordered recovery for a stateful dependency |
| 05.5 Node agents | DaemonSet log/metric collector and scheduling/resource trade-offs |
| 05.6 Access | least-privilege ServiceAccount, Role, RoleBinding and denied-API diagnosis |
| 05.7 Packaging | turn the baseline manifests into a Helm chart and compare with Kustomize overlays |
| 05.8 Scaling | HPA backed by a real metric; load generation and stabilization window |
| 05.9 Networking | Ingress, TLS, NetworkPolicy and CoreDNS/service troubleshooting |
| 05.10 Operations | image pull, CrashLoopBackOff, pending Pod, failed probe and resource-limit incident drills |

## Break/fix 05.1 — Service has no endpoints

Change the Service selector so it no longer matches the echo Deployment. Diagnose labels, EndpointSlices, DNS and connection behavior. Repair the selector and prove in-cluster traffic works.

## Break/fix 05.2 — Pod is CrashLoopBackOff

Deploy a configuration with a bad command or missing ConfigMap. Use `kubectl describe`, previous logs, events and the generated Pod specification before changing it. Repair the root cause and explain why deleting the Pod alone is not a fix.

## Break/fix 05.3 — Workload is denied despite a valid ServiceAccount

Bind a minimal Role that intentionally lacks one required verb. Use `kubectl auth can-i` and API error messages to add only the missing permission.
