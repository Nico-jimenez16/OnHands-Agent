from fastapi import FastAPI

from app.api.routes.health_routes import router as health_router
from app.config.settings import Settings
from app.observability.logging.logging_configuration import configure_logging


def create_application() -> FastAPI:
    """Build the Foundation application from current environment settings."""
    settings = Settings()
    configure_logging(settings.log_level)
    application = FastAPI(title=settings.app_name)
    application.include_router(health_router)
    return application


app = create_application()
