from app.modules.user_responsible_id.adapter import get_user_responsible_id
from app.modules.user_responsible_id.schemas import UserIDResponse

def user_responsible_id_service(token: str) -> UserIDResponse:
    if not token:
        raise Exception("Token de autenticação inválido ou ausente.")

    return get_user_responsible_id(token)
