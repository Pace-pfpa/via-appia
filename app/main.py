from fastapi import FastAPI
from app.core.http_client import fetch_data
from app.core.logger import logger
from app.core.settings import settings
from app.modules.login.controller import router as login_router

app = FastAPI(title="Via Appia API", version="1.0")

app.include_router(login_router)

@app.get("/id")
async def id_responsible_user():
    logger.info("Rota de id_usuário_responsável acessada.")
    pass

@app.post("/processos")
async def get_info_sapiens():
    logger.info("Rota de processos acessada.")
    pass

@app.post("/page")
async def read_doc_page():
    logger.info("Rota de ler_documento acessada.")
    pass
