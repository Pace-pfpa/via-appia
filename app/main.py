from fastapi import FastAPI
from app.modules.login.controller import router as login_router
from app.modules.user_responsible_id.controller import router as user_responsible_id_router

app = FastAPI(title="Via Appia API", version="1.0")

app.include_router(login_router)

app.include_router(user_responsible_id_router)
