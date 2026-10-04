# OnHands Agent Service
Backend Python + FastAPI del ecosistema OnHands. Este repositorio entrega Fase 0 — Foundation. Gateway/Auth Service es responsable de autenticación.

## Implemented
- Aplicación ASGI y factory FastAPI.
- `GET /health`: liveness local con contrato fijo.
- Settings tipados desde entorno/.env y logging centralizado en consola.
- pytest, especificaciones de fase y arquitectura con diez ADRs.

## Planned
OpenAI Agents SDK, proveedores LLM configurables, skills, tools, workflow state, sesiones, confirmaciones READ/WRITE, guardrails, SSE, tracing, metrics, evals y MongoDB para estado propio. No están implementados. V1 prevé un solo agente sin RAG/embeddings ni fallback automático.

## Instalación (PowerShell, Python 3.12 o superior)
Desde la raíz:
```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
Copy-Item .env.example .env
```
La invocación directa del intérprete evita depender de la política de activación de PowerShell. Para instalar sólo runtime, usar `pip install -e .` con ese intérprete.

## Configuración
| Variable | Default | Uso |
| --- | --- | --- |
| APP_NAME | onhands-agent-service | Título de FastAPI, no cambia la identidad de health |
| LOG_LEVEL | INFO | DEBUG, INFO, WARNING, ERROR o CRITICAL |

Las variables del proceso prevalecen sobre `.env`, leído desde el directorio de trabajo. Un valor inválido impide iniciar. `.env.example` contiene sólo valores de ejemplo; `.env` está ignorado. Logging de aplicación usa stderr con fecha, nivel, logger y mensaje; Uvicorn administra sus propios logs del servidor.

## Inicio y health
```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```
En otra terminal:
```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```
Responde HTTP 200:
```json
{"status": "healthy", "service": "onhands-agent-service"}
```
No verifica MongoDB, LLMs ni otros servicios. También hay documentación HTTP generada por FastAPI en `/docs`.

## Tests
```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## Estructura y especificaciones
```text
app/
  main.py
  api/routes/health_routes.py
  config/settings.py
  observability/logging/logging_configuration.py
tests/
  api/test_health_routes.py
  unit/test_settings.py
  unit/test_logging_configuration.py
spec/
  README.md
  architecture/{overview.md,decisions.md,diagrams.md,adr/}
  phase-00-foundation/{SPEC.md,DESIGN.md,PLAN.md,TESTS.md,REPORT.md}
AGENTS.md
pyproject.toml
.env.example
```
Consultar [guía de specs](spec/README.md), [arquitectura](spec/architecture/overview.md), [SPEC](spec/phase-00-foundation/SPEC.md) y [reporte de validación](spec/phase-00-foundation/REPORT.md). Seguir Spec-Driven Development + TDD; no avanzar a fases futuras sin especificación y aprobación.
