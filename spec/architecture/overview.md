# Arquitectura V1 prevista
Frontend → API Gateway → OnHands Agent Service → microservicios internos de OnHands.
Gateway/Auth Service autentican; Agent Service no administra autenticación propia.

Foundation implementa solamente Python, FastAPI, settings, logging y health. Todo lo siguiente está previsto, no implementado: OpenAI Agents SDK, proveedores LLM configurables, skills, tools, workflow state, sesiones, confirmaciones, guardrails, streaming SSE, tracing, metrics y evals. MongoDB almacenará exclusivamente estado propio del servicio en una fase posterior.

El LLM interpreta lenguaje e intención; el runtime controla el workflow; skills describen procedimientos; tools exponen capacidades; backend/domain services aplican reglas de negocio.
READ puede ejecutarse automáticamente; WRITE requiere confirmación explícita. User Service, Request Service, Provider Service y otros se consumen mediante APIs/clientes internos. Nunca se accede directamente a sus bases de datos.
V1 utiliza un solo agente, sin multi-agent, RAG, vector database, embeddings ni fallback automático entre proveedores LLM.
