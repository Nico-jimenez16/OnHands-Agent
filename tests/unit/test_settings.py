import pytest
from pydantic import ValidationError

from app.config.settings import Settings


@pytest.fixture(autouse=True)
def isolate_environment(monkeypatch):
    """Keep settings tests independent of the developer environment."""
    for name in ("APP_NAME", "LOG_LEVEL"):
        monkeypatch.delenv(name, raising=False)


def test_settings_defaults():
    """Essential configuration has usable defaults."""
    settings = Settings(_env_file=None)
    assert settings.app_name == "onhands-agent-service"
    assert settings.log_level == "INFO"


def test_settings_load_environment(monkeypatch):
    """Environment overrides are applied to typed settings."""
    monkeypatch.setenv("APP_NAME", "local-service")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    settings = Settings(_env_file=None)
    assert settings.app_name == "local-service"
    assert settings.log_level == "DEBUG"


def test_settings_load_dotenv_with_environment_precedence(tmp_path, monkeypatch):
    """A dotenv file supplies defaults while process environment wins."""
    environment_file = tmp_path / ".env"
    environment_file.write_text("APP_NAME=dotenv-service\nLOG_LEVEL=WARNING\n", encoding="utf-8")
    monkeypatch.setenv("LOG_LEVEL", "ERROR")
    settings = Settings(_env_file=environment_file)
    assert settings.app_name == "dotenv-service"
    assert settings.log_level == "ERROR"


@pytest.mark.parametrize("overrides", [{"log_level": "INVALID"}, {"app_name": ""}])
def test_settings_reject_invalid_values(overrides):
    """Invalid essential configuration fails immediately."""
    with pytest.raises(ValidationError):
        Settings(_env_file=None, **overrides)
