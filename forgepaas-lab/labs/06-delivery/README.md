# Lab 06 — Build systems and CI/CD

The initial GitHub Actions workflow in `.github/workflows/ci.yml` verifies the control plane and builds both images. Extend it only after it is green on every push.

## Required increments

1. Define branch protection and a build matrix that keeps unit tests fast.
2. Add dependency/image scanning and decide which findings block release.
3. Publish immutable image tags to a registry; use no long-lived cloud credentials in CI.
4. Add a local deployment promotion step with explicit environment approval semantics.
5. Apply a rolling update, observe readiness/availability, then perform a rollback from a recorded bad image tag.
6. Add release notes showing build input, image digest, deploy target and rollback command.

## Break/fix 06.1 — CI passes but the image cannot start

Make a change that satisfies unit tests but breaks the Docker runtime command. Add an image smoke test to CI and repair the pipeline gap.

## Break/fix 06.2 — A rollout stalls

Deploy an image whose readiness endpoint fails. Use Deployment conditions, ReplicaSets and events to decide whether to wait, fix forward, pause or roll back. Record the decision criteria.
