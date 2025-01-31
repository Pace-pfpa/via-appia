from fastapi import APIRouter, HTTPException
from app.modules.login.schemas import LoginRequest, LoginResponse
from app.modules.login.service import login_service
from app.core.logger import logger

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
def login(login_data: LoginRequest):
    logger.info("MACAXEIRA")
    try:
        token = login_service(login_data)
        if isinstance(token, dict) and "error" in token:
            logger.error(f"Erro no login: {token['error']}")
            raise HTTPException(status_code=400, detail=token["error"])

        return token

    except HTTPException as http_error:
        raise http_error

    except Exception as error:
        logger.error(f"Erro interno no servidor: {str(error)}")
        raise HTTPException(status_code=400, detail="Erro de autenticação. Email ou senha inválidos.")
