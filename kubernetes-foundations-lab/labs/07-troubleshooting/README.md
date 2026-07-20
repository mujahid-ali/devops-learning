# Lab 07 — Evidence-first troubleshooting

## Goal

Practice the debugging order before adding advanced Kubernetes features.

Read [the debugging order](../../docs/02-debugging-order.md), then work through the faults below. Do not read a fix until you can classify the problem and collect evidence.

## Fault 1 — ImagePullBackOff

```sh
kubectl apply -f manifests/breakfix/image-pull-backoff.yaml
kubectl get pod broken-image -n playground
kubectl describe pod broken-image -n playground
kubectl get events -n playground --sort-by=.lastTimestamp
```

Classify the error. Find the exact image reference Kubernetes attempted to pull. Repair by changing it to a known valid image, then delete/reapply or edit the manifest deliberately. Do not “fix” an image pull error by restarting unrelated cluster components.

## Fault 2 — Service resolves but has no endpoints

Repeat the broken-service exercise from Lab 05. Use this order:

1. Read the Service selector.
2. Read the Deployment’s Pod-template labels.
3. Inspect EndpointSlices.
4. Test DNS only after proving endpoint state.

## Fault 3 — Deleted managed Pod

Delete one Pod owned by `deployment/web`, then compare the before/after `kubectl get deployment,replicaset,pod` output. Explain why this is a healthy event, unlike deletion in Lab 03.

## Incident-note template

```text
Symptom:
Evidence (commands and relevant output):
Hypothesis:
Root cause:
Repair:
Prevention/alert or guardrail:
```

## Done when

You can decide whether a failure belongs to the API/context, scheduler/node, image/runtime, application, or Service/network layer before attempting a repair.
