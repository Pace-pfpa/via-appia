from fastapi import APIRouter

from app.modules.login.login_controller import router as login_router
from app.modules.buscar_user_responsible_id.uri_controller import router as user_responsible_id_router
from app.modules.buscar_processos_id.pid_controller import router as buscar_processo_id_router
from app.modules.create_tarefas.create_tarefas_controller import router as create_tarefas_router

router = APIRouter()

router.include_router(login_router)
router.include_router(user_responsible_id_router)
router.include_router(buscar_processo_id_router)
router.include_router(create_tarefas_router)
