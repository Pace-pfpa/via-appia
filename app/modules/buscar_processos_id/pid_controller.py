from fastapi import APIRouter, HTTPException, Header
from app.modules.buscar_processos_id.pid_schema import ProcessosIdRequest, ProcessosIdResponse
from app.modules.buscar_processos_id.pid_service import buscar_processos_id_service
from app.core.logger import logger

router = APIRouter()

@router.post("/buscar_id_processos", response_model=ProcessosIdResponse)
def buscar_processos_id(request: ProcessosIdRequest, authorization: str = Header(None)):

    if not authorization or not authorization.startswith("Bearer "):
        logger.error("Erro na autorização.")
        raise HTTPException(status_code=401, detail="Token inválido ou ausente.")

    token = authorization.split(" ")[1]

    try:
        return buscar_processos_id_service(request.numeros_processos, token)

    except HTTPException as http_error:
        raise http_error

    except Exception as error:
        logger.error(f"Erro interno no servidor: {str(error)}")
        raise HTTPException(status_code=400, detail=str(error))
