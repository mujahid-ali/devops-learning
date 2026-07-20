"""The first, intentionally small, ForgePaaS control-plane API."""

import logging
import os
from threading import Lock
from typing import Dict, List

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest


logger = logging.getLogger("forgepaas.control_plane")
logging.basicConfig(
    level=os.getenv("PLATFORM_LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

APP_CREATIONS = Counter(
    "forgepaas_app_registrations_total",
    "Number of desired-state application registrations accepted by the control plane.",
)


class ApplicationSpec(BaseModel):
    """Desired state accepted now and reconciled into Kubernetes in a later lab."""

    name: str = Field(pattern=r"^[a-z][a-z0-9-]{2,30}$")
    image: str = Field(min_length=3, max_length=255)
    replicas: int = Field(default=1, ge=1, le=10)
    port: int = Field(default=8080, ge=1, le=65535)


class ApplicationStore:
    """Thread-safe in-memory store that will be replaced by PostgreSQL in Lab 03."""

    def __init__(self) -> None:
        self._apps: Dict[str, ApplicationSpec] = {}
        self._lock = Lock()

    def create(self, spec: ApplicationSpec) -> ApplicationSpec:
        with self._lock:
            if spec.name in self._apps:
                raise KeyError(spec.name)
            self._apps[spec.name] = spec
        return spec

    def get(self, name: str) -> ApplicationSpec:
        with self._lock:
            try:
                return self._apps[name]
            except KeyError as exc:
                raise KeyError(name) from exc

    def list(self) -> List[ApplicationSpec]:
        with self._lock:
            return list(self._apps.values())


store = ApplicationStore()
app = FastAPI(title="ForgePaaS Control Plane", version="0.1.0")


@app.get("/healthz", tags=["platform"])
def healthz() -> dict:
    """Liveness: this process can answer requests."""
    return {"status": "ok", "service": "control-plane"}


@app.get("/readyz", tags=["platform"])
def readyz() -> dict:
    """Readiness is deliberately process-only until dependencies are integrated."""
    return {"status": "ready", "checks": {"process": "pass", "persistence": "not-integrated"}}


@app.get("/metrics", tags=["platform"], include_in_schema=False)
def metrics() -> Response:
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.post("/api/v1/apps", status_code=status.HTTP_201_CREATED, tags=["applications"])
def create_application(spec: ApplicationSpec) -> ApplicationSpec:
    """Register desired state. No Kubernetes reconciliation is claimed at this stage."""
    try:
        created = store.create(spec)
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An application with that name already exists.",
        )
    APP_CREATIONS.inc()
    logger.info("application_registered name=%s replicas=%s", created.name, created.replicas)
    return created


@app.get("/api/v1/apps", tags=["applications"])
def list_applications() -> List[ApplicationSpec]:
    return store.list()


@app.get("/api/v1/apps/{name}", tags=["applications"])
def get_application(name: str) -> ApplicationSpec:
    try:
        return store.get(name)
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found.")
