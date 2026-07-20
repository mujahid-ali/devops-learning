SHELL := /bin/sh

.DEFAULT_GOAL := help

.PHONY: help verify render status delete

help: ## Show optional helpers; create the cluster manually in Lab 01.
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z0-9_-]+:.*##/ {printf "%-10s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

verify: ## Validate YAML structure locally; it does not create a cluster.
	kubectl kustomize manifests >/dev/null

render: ## Print the Kubernetes objects in the order they will be applied.
	kubectl kustomize manifests

status: ## Show only the Step 1 cluster and its learner namespace.
	kubectl --context kind-k8s-foundations get nodes
	kubectl --context kind-k8s-foundations -n playground get all

delete: ## Delete only the disposable k8s-foundations kind cluster.
	kind delete cluster --name k8s-foundations
