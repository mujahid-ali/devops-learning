# Lab 08 — Graduation to ForgePaaS (Step 2)

Move to Step 2 only after you can demonstrate the following without a script:

- Create and delete a named kind cluster and identify its Docker node containers.
- Explain the API server → etcd → scheduler → kubelet → container-runtime path.
- Create a namespace, naked Pod, Deployment, Service, ConfigMap and fake Secret one at a time.
- Explain labels/selectors, desired versus actual state, Service DNS and NodePort traffic.
- Diagnose an invalid image and a Service with no endpoints using events, `describe`, logs and EndpointSlices.
- Perform a controlled rolling update and rollback.

When these are comfortable, start [ForgePaaS Lab](../../forgepaas-lab/README.md). Its first Kubernetes exercises will make much more sense: you will be able to reason about its control plane, probes, resources, Services and kind bootstrap instead of treating them as prebuilt machinery.

Keep the `k8s-foundations` cluster during your first ForgePaaS sessions only if Docker Desktop has enough memory. Otherwise delete it and recreate it whenever you want to repeat the fundamentals.
