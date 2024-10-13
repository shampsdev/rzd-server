from fastapi import FastAPI
from .health.api import router as health_router
from .recognition.api import router as recognition_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(prefix="/health", router=health_router)
app.include_router(prefix="/recognition", router=recognition_router)
