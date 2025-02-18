from fastapi import APIRouter, HTTPException, Header
from app.modules.create_tarefa.create_tarefa_schema import CreateTarefaRequest, CreateTarefaSupersapiensResponse
from app.modules.create_tarefa.create_tarefa_service import create_tarefa_service
from app.core.logger import logger

router = APIRouter()

@router.post("/create_tarefa", response_model=CreateTarefaSupersapiensResponse)
async def criar_tarefa(tarefa_data: CreateTarefaRequest, authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        logger.error(f"Erro na autorização: {authorization}")
        raise HTTPException(status_code=401,
                            detail="Token inválido ou ausente.")

    token = authorization.split(" ")[1]

    try:
        return create_tarefa_service(tarefa_data, token)

    except HTTPException as http_error:
        raise http_error

    except Exception as error:
        logger.error(f"Erro interno no servidor: {str(error)}")
        raise HTTPException(status_code=400, detail=str(error))