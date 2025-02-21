from fastapi import APIRouter, HTTPException, Header
from app.modules.create_tarefas.create_tarefas_schema import CreateTarefasRequestNewPace, CreateTarefasSupersapiensResponse
from app.modules.create_tarefas.create_tarefas_service import create_tarefas_service
from app.core.logger import logger

router = APIRouter()

@router.post("/create_tarefas", response_model=CreateTarefasSupersapiensResponse)
async def criar_tarefas(request_data: CreateTarefasRequestNewPace, authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        logger.error("Erro na autorização.")
        raise HTTPException(status_code=401, detail="Token inválido ou ausente.")

    token = authorization.split(" ")[1]

    try:
        return create_tarefas_service(request_data, token)

    except HTTPException as http_error:
        raise http_error

    except Exception as error:
        logger.error(f"Erro interno no servidor: {str(error)}")
        raise HTTPException(status_code=400, detail=str(error))
