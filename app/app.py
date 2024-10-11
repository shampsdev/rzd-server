from fastapi import FastAPI
from .health.api import router as health_router
from .recognition.api import router as recognition_router

app = FastAPI()

app.include_router(prefix="/health", router=health_router)
app.include_router(prefix="/recognition", router=recognition_router)
