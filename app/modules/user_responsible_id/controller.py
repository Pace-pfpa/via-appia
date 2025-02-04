from fastapi import APIRouter, HTTPException, Header
from app.core.logger import logger
from app.modules.user_responsible_id.schemas import UserIDResponse
from app.modules.user_responsible_id.service import user_responsible_id_service

router = APIRouter()

@router.get("/id", response_model=UserIDResponse)
def user_responsible_id(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        logger.error(f"Erro na autorização: {authorization}")
        raise HTTPException(status_code=401,
                            detail="Token inválido ou ausente.")

    token = authorization.split(" ")[1]

    try:
        return user_responsible_id_service(token)

    except HTTPException as http_error:
        raise http_error

    except Exception as error:
        logger.error(f"Erro interno no servidor: {str(error)}")
        raise HTTPException(status_code=400, detail=str(error))