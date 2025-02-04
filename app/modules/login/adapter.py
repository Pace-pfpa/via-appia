import requests
from app.core.settings import settings
from app.core.logger import logger

def authenticate(email: str, password: str):
    url = f"{settings.URL_API_SS}/auth/ldap_get_token"
    payload = {"username": email, "password": password}

    try:
        response = requests.request("POST", url, json=payload)
        token = response.json()["token"]
        return token

    except requests.RequestException as e:
        logger.error(f"Erro ao autenticar no Supersapiens: {str(e)}")
        return {"error": f"Erro ao autenticar no Supersapiens: {str(e)}"}
