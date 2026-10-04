# Fase 0 — Foundation
## Objetivo y alcance
Entregar una aplicación Python + FastAPI ejecutable, configuración tipada por entorno, logging centralizado, pytest, documentación arquitectónica, ADRs, AGENTS.md, README y .env.example.
## Contratos verificables
- `app.main:app` es importable y `create_application()` crea una aplicación FastAPI.
- `GET /health` responde HTTP 200 y JSON exactamente `{"status": "healthy", "service": "onhands-agent-service"}`. Es liveness local, sin consultar dependencias externas.
- Settings acepta `APP_NAME` (título de aplicación; no altera la identidad contractual de health) y `LOG_LEVEL` (DEBUG, INFO, WARNING, ERROR, CRITICAL), con defaults onhands-agent-service e INFO. Valores inválidos fallan al cargar configuración.
- Logging configura el nivel del logger raíz y un handler de consola, con fecha, nivel, logger y mensaje; no acumula handlers propios al repetirse.
- Todos los tests deben pasar y Uvicorn debe servir health realmente.
## Fuera de alcance
Agente, LLMs, tools, skills, MongoDB, sesiones, streaming, autenticación, lógica de negocio y componentes de fases futuras.
## Definition of Done
Proyecto instalable; inicio HTTP real; health 200; settings y logging funcionales; suite verde; spec completa; arquitectura V1 y diez ADRs; AGENTS.md, README y .env.example; sin secretos, código muerto evidente ni capacidades futuras implementadas. REPORT sólo se completa después de validación.
