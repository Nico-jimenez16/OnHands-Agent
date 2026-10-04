# Guía de desarrollo
OnHands Agent Service es un backend Python/FastAPI; Foundation sólo proporciona infraestructura mínima.
Arquitectura: Frontend → Gateway/Auth → Agent Service → APIs de microservicios. Autenticación pertenece al Gateway/Auth. El servicio nunca accede directamente a DBs ajenas; utiliza APIs/clientes internos. Backend/domain services aplican reglas de negocio. V1 prevé un solo agente sin RAG ni fallback automático.

Seguir SPEC → DESIGN → PLAN → TESTS → IMPLEMENTATION → VALIDATION → REPORT y TDD RED → GREEN → REFACTOR → FULL TEST SUITE para código determinístico. Documentar antes de implementar y registrar evidencia real. `spec/architecture/` contiene contexto, decisiones, diagramas y ADRs; `spec/phase-XX-*/` contiene documentos de fase.
Usar nombres descriptivos, type hints, funciones pequeñas y enfocadas, imports claros, configuración centralizada y docstrings/comentarios breves para funciones propias relevantes. Evitar abstracciones innecesarias, código muerto y placeholders.
Probar contratos y comportamiento significativo; aislar entorno, ejecutar suite completa al cerrar. Actualizar specs y ADRs cuando cambie arquitectura y REPORT al cerrar cada fase; COMPLETED requiere Definition of Done validada.
READ puede ser automático; WRITE requiere confirmación explícita en el workflow del agente futuro. Esta política no agrega un paso de aprobación para cambios de desarrollo ya solicitados.
**No implementar funcionalidades de fases futuras sin que estén especificadas y aprobadas.**
Nunca guardar secretos ni .env real en el repositorio.
