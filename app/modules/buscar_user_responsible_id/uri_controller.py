from fastapi import APIRouter, HTTPException, Header
from app.modules.buscar_user_responsible_id.uri_schema import UserIDResponse
from app.modules.buscar_user_responsible_id.uri_service import buscar_responsible_id_service
from app.core.logger import logger

router = APIRouter()

@router.get("/id", response_model=UserIDResponse)
def buscar_user_responsible_id(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        logger.error(f"Erro na autorização: {authorization}")
        raise HTTPException(status_code=401,
                            detail="Token inválido ou ausente.")

    token = authorization.split(" ")[1]

    try:
        return buscar_responsible_id_service(token)

    except HTTPException as http_error:
        raise http_error

    except Exception as error:
        logger.error(f"Erro interno no servidor: {str(error)}")
        raise HTTPException(status_code=400, detail=str(error))
