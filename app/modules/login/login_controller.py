from fastapi import APIRouter, HTTPException
from app.modules.login.login_schema import LoginRequest, LoginResponse
from app.modules.login.login_service import login_service
from app.core.logger import logger

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
def login_ss(login_data: LoginRequest):
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
