# Diseño Foundation
Repositorio inspeccionado: carpeta vacía, sin Git, configuración ni tests existentes. Python 3.12 disponible.

Estructura mínima: `app/main.py`, `app/api/routes/health_routes.py`, `app/config/settings.py`, `app/observability/logging/logging_configuration.py`; tests en `tests/unit/` y `tests/api/`.
FastAPI expone una factory y una instancia ASGI. Un APIRouter implementa health con modelo de respuesta tipado de literales para fijar el contrato. Pydantic Settings carga entorno y .env UTF-8; sólo APP_NAME y LOG_LEVEL. Se permite un .env con variables adicionales sin usarlas. No se cachean settings: cada factory puede leer el entorno actual.
Logging usa biblioteca estándar, un handler propio en stderr y formatter centralizado. Mantiene handlers ajenos y evita duplicar el propio. La factory configura logging antes de retornar la aplicación.
`pyproject.toml` define empaquetado setuptools, Python >=3.12, dependencias FastAPI, pydantic-settings y Uvicorn; extra dev pytest/httpx. pytest descubre tests desde tests/. Entorno virtual local ignorado. README documenta comandos PowerShell y ASGI.
Pruebas: factory/import, health exacto, defaults/env/.env/validación de settings y emisión/nivel/idempotencia de logging. Smoke test inicia Uvicorn local y consulta HTTP real.
Sin carpetas ni configuraciones para capacidades futuras.
