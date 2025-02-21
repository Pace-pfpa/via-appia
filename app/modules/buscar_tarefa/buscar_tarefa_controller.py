from fastapi import APIRouter, HTTPException, Header, Path
from app.modules.buscar_tarefa.buscar_tarefa_schema import BuscarTarefaResponse
from app.modules.buscar_tarefa.buscar_tarefa_service import buscar_tarefa_service
from app.core.logger import logger

router = APIRouter()

@router.get('/buscar_tarefa', response_model=BuscarTarefaResponse)
def buscar_tarefa(
    idTarefa: int = Path(..., description="ID da tarefa a ser buscada"),
    authorization: str = Header(None)
):
    if not authorization or not authorization.startswith("Bearer "):
        logger.error(f"Erro na autorização: {authorization}")
        raise HTTPException(status_code=401,
                            detail="Token inválido ou ausente.")

    token = authorization.split(" ")[1]

    try:
        tarefa = buscar_tarefa_service(idTarefa, token)
        logger.info(f"Resposta da API Supersapiens: {tarefa}")
        return tarefa

    except HTTPException as http_error:
        raise http_error

    except Exception as error:
        logger.error(f"Erro interno no servidor: {str(error)}")
        raise HTTPException(status_code=400, detail="Erro de autenticação. Id inválido.")