"""Dependency-free tenant workload used to learn container and K8s operations."""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Lock


REQUESTS = 0
REQUESTS_LOCK = Lock()
SERVICE_NAME = os.getenv("SERVICE_NAME", "echo-service")
SERVICE_VERSION = os.getenv("SERVICE_VERSION", "dev")


class Handler(BaseHTTPRequestHandler):
    def _json(self, status_code: int, body: dict) -> None:
        payload = json.dumps(body).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
        global REQUESTS
        with REQUESTS_LOCK:
            REQUESTS += 1
        if self.path in ("/", "/healthz", "/readyz"):
            self._json(200, {"status": "ok", "service": SERVICE_NAME, "version": SERVICE_VERSION})
        elif self.path == "/metrics":
            payload = (
                "# HELP echo_service_requests_total Total HTTP requests handled.\n"
                "# TYPE echo_service_requests_total counter\n"
                f"echo_service_requests_total {REQUESTS}\n"
            ).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; version=0.0.4")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
        else:
            self._json(404, {"status": "not_found"})

    def log_message(self, fmt: str, *args: object) -> None:
        print(f"{self.client_address[0]} {fmt % args}", flush=True)


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
