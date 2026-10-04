from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    """Stable liveness contract independent of external services."""

    status: Literal["healthy"] = "healthy"
    service: Literal["onhands-agent-service"] = "onhands-agent-service"


@router.get("/health", response_model=HealthResponse)
def get_health() -> HealthResponse:
    """Report that the HTTP process can handle requests."""
    return HealthResponse()
