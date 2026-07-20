# Kubernetes debugging order

Avoid changing YAML until you have evidence. Work from cluster to workload:

1. **Context and API:** `kubectl config current-context`, `kubectl cluster-info`, `kubectl get --raw=/readyz`.
2. **Node capacity/readiness:** `kubectl get nodes -o wide`, then `kubectl describe node <node>`.
3. **Object intent/status:** `kubectl get <kind> -n <namespace> -o yaml` and `kubectl describe`.
4. **Events:** `kubectl get events -n <namespace> --sort-by=.lastTimestamp`.
5. **Logs:** `kubectl logs`, adding `--previous` after a restart.
6. **Networking:** labels, EndpointSlices, Service DNS, port numbers and NetworkPolicy.
7. **Inside the node only when needed:** `docker exec` followed by `crictl`, CNI configuration or kubelet logs.

For each fault, state whether it is a desired-state error, scheduling/resource error, image/runtime error, application error, or networking error. That classification is more useful than a list of commands.
