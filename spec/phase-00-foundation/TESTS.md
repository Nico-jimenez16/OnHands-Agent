# Estrategia de tests
Antes de implementación:
- Import y factory generan FastAPI.
- GET /health devuelve 200, application/json y contrato exacto.
- Settings: defaults determinísticos, carga del entorno y .env, rechazo de nivel inválido y nombre vacío.
- Logging: nivel configurado, emisión con formato y ausencia de duplicación del handler propio.
Usar TestClient para HTTP y monkeypatch para aislar entorno; no contactar servicios externos.
Validación adicional: suite completa e inicio real de Uvicorn con petición HTTP local.
## Evidencia
Pendiente de ejecutar RED → GREEN y validación final.

RED (2026-10-04): `python -m pytest -q` terminó con exit code 1 y tres errores de colección `ModuleNotFoundError: No module named app`, esperados porque aún no existía implementación. Los tests se escribieron y ejecutaron antes del código.

GREEN inicial: 8 passed, 1 warning. Se agregó una prueba significativa de integración settings/factory que comprueba título configurable e identidad health fija.
Refactor review: funciones pequeñas, responsabilidades separadas y sin abstracciones adicionales; no fue necesario refactor de producción.
FULL TEST SUITE final: 9 passed, 1 warning (1.04 s), exit code 0.
`python -m pip check`: No broken requirements found.
`python -m compileall -q app tests`: exit code 0.
Smoke HTTP real: Uvicorn iniciado como subprocess en localhost con puerto libre; GET /health devolvió 200 y contrato exacto. Proceso terminado al finalizar la comprobación.
Paquete editable reinstalado después de crear app y comprobado mediante import desde fuera del workspace: PASS.
Advertencia conocida: Starlette 1.7.0 depreca HTTPX en TestClient y recomienda HTTPX2. No afecta los resultados actuales; revisar compatibilidad en mantenimiento futuro.
