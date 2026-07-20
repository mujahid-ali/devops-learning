#!/usr/bin/env sh
set -eu

PROJECT_ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
CLUSTER_NAME=forgepaas

need() {
  if ! command -v "$1" >/dev/null 2>&1; then
    printf '%s\n' "Required command not found: $1" >&2
    exit 1
  fi
}

need docker
need kind
need kubectl

if ! docker info >/dev/null 2>&1; then
  printf '%s\n' 'Docker Desktop is not ready. Start it, wait for its engine, then retry.' >&2
  exit 1
fi

if ! kind get clusters | grep -qx "$CLUSTER_NAME"; then
  kind create cluster --name "$CLUSTER_NAME" --config "$PROJECT_ROOT/infra/local/kind/kind-config.yaml"
fi

docker build -t forgepaas/control-plane:dev "$PROJECT_ROOT/control-plane"
docker build -t forgepaas/echo-service:dev "$PROJECT_ROOT/sample-apps/echo-service"
kind load docker-image --name "$CLUSTER_NAME" forgepaas/control-plane:dev forgepaas/echo-service:dev

kubectl apply -k "$PROJECT_ROOT/k8s/overlays/local"
kubectl -n forgepaas rollout status deployment/control-plane --timeout=120s
kubectl -n forgepaas rollout status deployment/echo-service --timeout=120s

printf '%s\n' 'Platform is ready. Inspect it with: kubectl -n forgepaas get pods,svc'
