from fastapi import FastAPI
from .cats.api import router as cats_router

app = FastAPI()

app.include_router(prefix="/cats", router=cats_router)
