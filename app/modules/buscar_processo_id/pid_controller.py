from fastapi import APIRouter, HTTPException, Header
from app.modules.buscar_processo_id.pid_schema import ProcessoIdRequest, ProcessoIdResponse
from app.modules.buscar_processo_id.pid_service import buscar_processo_id_service
from app.core.logger import logger

router = APIRouter()

@router.get("/buscar_id_processo", response_model=ProcessoIdResponse)
def buscar_processo_id_controller(request: ProcessoIdRequest, authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        logger.error(f"Erro na autorização: {authorization}")
        raise HTTPException(status_code=401,
                            detail="Token inválido ou ausente.")

    token = authorization.split(" ")[1]

    try:
        return buscar_processo_id_service(request.nup, token)

    except HTTPException as http_error:
        raise http_error

    except Exception as error:
        logger.error(f"Erro interno no servidor: {str(error)}")
        raise HTTPException(status_code=400, detail=str(error))