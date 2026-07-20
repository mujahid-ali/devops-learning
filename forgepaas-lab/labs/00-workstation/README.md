# Lab 00 — Workstation and evidence

## Outcome

Prove that the local platform can be started, inspected and removed without relying on undocumented machine state.

## Checklist

1. Start Docker Desktop and prove it with `docker info`.
2. Install kind, then record `kind version`, `kubectl version --client`, `docker version` and the current Kubernetes context.
3. Run `make test`, `make up`, `curl http://localhost:8000/healthz`, and `make kind-up`.
4. Inspect a Pod, a Deployment, a Service, container logs and Kubernetes events. Record the difference between Compose and Kubernetes logs.
5. Create a `notes/` directory that is ignored locally or has only sanitized examples. Never store private keys, tokens or cloud credentials.

## Break/fix 00.1 — Docker engine unavailable

**Inject:** Quit Docker Desktop, then run `make up`.

**Investigate:** Identify the client-versus-daemon error. Confirm whether the Docker socket exists and whether the engine is ready.

**Done when:** You can start the engine, rerun the command, and explain why installing the Docker CLI alone would not solve the problem.

## Break/fix 00.2 — Wrong Kubernetes context

**Inject:** After a kind cluster exists, deliberately change context away from it (or use a harmless nonexistent context for the command).

**Investigate:** Use `kubectl config current-context`, `kubectl cluster-info`, and a namespace-scoped read command before changing anything.

**Done when:** You have a pre-flight checklist that prevents deploying to the wrong cluster.
