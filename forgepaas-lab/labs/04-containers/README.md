# Lab 04 — Docker and image engineering

Use `control-plane/` and `sample-apps/echo-service/` as the two images. Inspect every layer and run each image as a non-root user where practical.

1. Build tagged images; compare immutable tag and mutable `dev` tag trade-offs.
2. Add `.dockerignore`, deterministic dependency installation and a multi-stage production build for the control plane.
3. Use Compose networks, service DNS, PostgreSQL volume persistence and log inspection.
4. Apply CPU/memory limits and observe cgroup behavior from Lab 01.
5. Document image provenance, SBOM/scan choice and secret-handling rules for CI.

## Break/fix 04.1 — Container exits immediately

Replace an entrypoint or command with an invalid module/path. Diagnose `docker inspect`, exit code, logs, image filesystem and working directory; repair without adding a sleep loop.

## Break/fix 04.2 — Service works on the host but not from another container

Bind a test service to loopback or use the wrong Compose hostname. Prove the namespace/network difference, then use the service DNS name and correct bind address.

## Break/fix 04.3 — Data disappears after a rebuild

Run PostgreSQL without its named volume in a disposable environment. Identify the container lifecycle mistake and repair it with an explicit volume plus a backup/restore note.
