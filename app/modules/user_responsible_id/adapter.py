import requests
from app.core.settings import settings
from app.core.logger import logger
from app.modules.user_responsible_id.schemas import UserIDResponse


def get_user_responsible_id(token: str) -> UserIDResponse:
    url = f"{settings.URL_API_SS}/profile"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.request("GET", url, headers=headers)
        data = response.json()
        return UserIDResponse(id=data["id"])

    except requests.RequestException as e:
        logger.error(f"Erro ao obter o ID do usuário: {str(e)}")
        raise Exception(f"Erro ao obter o ID do usuário: {str(e)}")
