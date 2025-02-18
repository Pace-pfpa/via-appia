from fastapi import FastAPI

from app.modules.login.login_controller import router as login_router
from app.modules.buscar_user_responsible_id.uri_controller import router as user_responsible_id_router
from app.modules.buscar_processo_id.pid_controller import router as  buscar_processo_id_router
from app.modules.create_tarefa.create_tarefa_controller import router as create_tarefa_router

app = FastAPI(title="Via Appia API", version="1.0")

app.include_router(login_router)

app.include_router(user_responsible_id_router)

app.include_router(buscar_processo_id_router)

app.include_router(create_tarefa_router)