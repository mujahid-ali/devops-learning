SHELL := /bin/sh

.DEFAULT_GOAL := help

.PHONY: help up down logs test check kind-up kind-delete status

help: ## Show supported local actions.
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z0-9_-]+:.*##/ {printf "%-14s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

up: ## Start the local control plane, PostgreSQL, and Redis.
	docker compose up --build -d

down: ## Stop local Compose services while preserving named volumes.
	docker compose down

logs: ## Follow the control-plane logs.
	docker compose logs -f control-plane

test: ## Run control-plane tests inside its Docker image.
	docker compose run --build --rm control-plane pytest -q

check: ## Syntax-check Python without requiring installed dependencies.
	python3 -c 'from pathlib import Path; roots = (Path("control-plane/app"), Path("control-plane/tests"), Path("sample-apps/echo-service/app")); files = [source for root in roots for source in root.rglob("*.py")]; [compile(source.read_text(), str(source), "exec") for source in files]; print(f"Syntax check passed for {len(files)} Python files.")'

kind-up: ## Create the local kind platform and deploy baseline workloads.
	./scripts/bootstrap-kind.sh

kind-delete: ## Delete only the disposable forgepaas kind cluster.
	kind delete cluster --name forgepaas

status: ## Show local Compose services and platform Kubernetes objects.
	docker compose ps
	@kubectl -n forgepaas get deployments,pods,services 2>/dev/null || true
