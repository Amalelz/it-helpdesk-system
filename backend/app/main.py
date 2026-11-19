from fastapi import FastAPI

from app.core.config import settings
from app.routers import auth, health

app = FastAPI(title=settings.app_name, version="0.1.0")
app.include_router(health.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")