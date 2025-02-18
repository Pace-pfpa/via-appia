import requests
from app.core.settings import settings
from app.core.logger import logger

def buscar_processo_id_adapter(nup:str, token: str):
    url = f"{settings.URL_API_SS}/v1/administrativo/process"
    params = {"where": f'{{"NUP": "eq:{nup}"}}'}
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.request("GET", url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        logger.info(f"Resposta da API Supersapiens: {data}")

        return data[0]

    except requests.RequestException as e:
        logger.error(f"Erro ao buscar processo por NUP: {str(e)}")
        raise Exception(f"Erro ao ao buscar processo por NUP: {str(e)}")
