from app.modules.buscar_user_responsible_id.uri_adapter import buscar_user_responsible_id_adapter
from app.modules.buscar_user_responsible_id.uri_schema import UserIDResponse

def buscar_responsible_id_service(token: str) -> UserIDResponse:
    if not token:
        raise Exception("Token de autenticação inválido ou ausente.")

    return buscar_user_responsible_id_adapter(token)
