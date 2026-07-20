# Lab 07 — Observability

Use the `/metrics` endpoints as the starting point. Add Prometheus, Grafana and Loki only after you can explain one useful metric, one useful log field and one correlation path.

## Deliverables

1. Prometheus scrape configuration and dashboards for request rate, errors, latency, saturation and deployment health.
2. Structured control-plane logs with request/correlation IDs and secret redaction.
3. Centralized Kubernetes log collection in Loki (or a documented equivalent) with a dashboard link/runbook query.
4. Alert rules for unavailable control plane, failing rollouts, high error rate and resource saturation.
5. A service-level objective with an error budget and an explanation of which alert is page-worthy.

## Break/fix 07.1 — Dashboard is green while the service is failing

Break the metric label/query or make a probe fail without increasing the chosen application counter. Diagnose the blind spot, repair the metric/query, and add an alert that detects the user-visible failure.

## Break/fix 07.2 — Logs cannot identify the affected request

Generate concurrent requests without a correlation ID. Add a safe request identifier propagated through logs and show a single request’s path without logging credentials or personal data.
