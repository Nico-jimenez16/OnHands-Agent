import pytest

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import app, create_application


@pytest.fixture(autouse=True)
def isolate_application_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """Give each application factory deterministic settings."""
    monkeypatch.setenv("APP_NAME", "onhands-agent-service")
    monkeypatch.setenv("LOG_LEVEL", "INFO")


def test_application_can_be_imported_and_created():
    """Verify both supported ASGI entry points."""
    assert isinstance(app, FastAPI)
    assert isinstance(create_application(), FastAPI)


def test_health_has_stable_liveness_contract():
    """Health reports local process availability with the agreed identity."""
    with TestClient(create_application()) as client:
        response = client.get("/health")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"status": "healthy", "service": "onhands-agent-service"}


def test_application_uses_settings_without_changing_health(monkeypatch: pytest.MonkeyPatch) -> None:
    """Configured application title never changes the stable service identity."""
    monkeypatch.setenv("APP_NAME", "local-service")
    application = create_application()
    assert application.title == "local-service"
    with TestClient(application) as client:
        assert client.get("/health").json()["service"] == "onhands-agent-service"
