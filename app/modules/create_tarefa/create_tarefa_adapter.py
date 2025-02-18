import requests
from app.core.settings import settings
from app.core.logger import logger
from app.modules.create_tarefa.create_tarefa_schema import CreateTarefaRequest

def create_tarefa_adapter(tarefa_data: CreateTarefaRequest, token: str):
    url = f"{settings.URL_API_SS}/v1/administrativo/tarefa"
    headers = {"Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
    }

    try:
        payload = tarefa_data.model_dump(mode="json")
        response = requests.request("POST", url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        logger.error(f"Erro ao criar tarefa: {str(e)}")
        raise Exception(f"Erro ao criar tarefa: {str(e)}")