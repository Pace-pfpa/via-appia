from app.modules.login.login_adapter import authenticate
from app.modules.login.login_schema import LoginRequest, LoginResponse
from app.core.logger import logger

def login_service(login_data: LoginRequest):
    response = authenticate(login_data.email, login_data.password)
    logger.info(response)

    return LoginResponse(token=response)



