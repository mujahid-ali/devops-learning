# Lab 05 — Service, labels, DNS and NodePort

## Goal

Give a changing set of Deployment Pods a stable access point, then follow traffic from your browser to a Pod.

## Create the Service

```sh
kubectl apply -f manifests/03-service/web-service.yaml
kubectl get service,endpointslice -n playground
kubectl describe service web -n playground
curl -i http://localhost:8080
```

The flow is:

```text
browser → localhost:8080 → Docker port mapping → worker NodePort 30080
→ Service selector (app=web) → ready Pod endpoint → NGINX container port 80
```

The `extraPortMappings` entry in `kind/cluster.yaml` created only the host-to-worker part. Kubernetes creates the NodePort/Service part after you apply the Service manifest.

## Prove service DNS

Launch a temporary in-cluster diagnostic Pod, resolve the Service, then remove it automatically:

```sh
kubectl run dns-test -n playground --image=busybox:1.36 --restart=Never --rm -it -- nslookup web
```

Repeat with `web.playground` and `web.playground.svc.cluster.local`. This demonstrates CoreDNS resolving a Service name, not the address of an individual Pod.

## Break/fix — Service with no endpoints

Apply the deliberately faulty service:

```sh
kubectl apply -f manifests/breakfix/service-with-no-endpoints.yaml
kubectl get endpointslice -n playground
kubectl describe service broken-web -n playground
```

Compare its selector to the Deployment’s Pod labels. Repair it only after recording why DNS can resolve a Service that has no healthy endpoints.

## Done when

You can explain why a Service has a stable name while Pod IPs can change, and distinguish `port`, `targetPort`, `nodePort`, and `hostPort`.
