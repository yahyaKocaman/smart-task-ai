from fastapi import FastAPI
from app.infrastructure.database import Base, engine
from app.api import auth, tasks
from prometheus_fastapi_instrumentator import Instrumentator
from app.core.logging import setup_logging

app = FastAPI(title="Smart Task AI Microservice")

# Logging setup
setup_logging()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth")
app.include_router(tasks.router, prefix="/tasks")

Instrumentator().instrument(app).expose(app)

@app.get("/health")
def health():
    return {"status": "ok"}