from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Via Appia API", version="1.0")

app.include_router(router)
