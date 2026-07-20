from fastapi.testclient import TestClient

from app.main import app, store


client = TestClient(app)


def setup_function() -> None:
    # The temporary store is intentionally reset between unit tests.
    store._apps.clear()  # noqa: SLF001 - replacement persistence is a future exercise.


def test_health_and_readiness_endpoints() -> None:
    assert client.get("/healthz").json()["status"] == "ok"
    body = client.get("/readyz").json()
    assert body["status"] == "ready"
    assert body["checks"]["persistence"] == "not-integrated"


def test_register_and_get_application() -> None:
    payload = {"name": "echo-api", "image": "forgepaas/echo-service:dev", "replicas": 2}
    created = client.post("/api/v1/apps", json=payload)
    assert created.status_code == 201
    assert created.json()["replicas"] == 2

    fetched = client.get("/api/v1/apps/echo-api")
    assert fetched.status_code == 200
    assert fetched.json()["image"] == payload["image"]


def test_reject_duplicate_and_invalid_names() -> None:
    payload = {"name": "echo-api", "image": "forgepaas/echo-service:dev"}
    assert client.post("/api/v1/apps", json=payload).status_code == 201
    assert client.post("/api/v1/apps", json=payload).status_code == 409
    assert client.post("/api/v1/apps", json={"name": "INVALID", "image": "test"}).status_code == 422
