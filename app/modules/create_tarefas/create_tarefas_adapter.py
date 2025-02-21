import requests
from app.core.settings import settings
from app.core.logger import logger
from app.modules.create_tarefas.create_tarefas_schema import CreateTarefasRequest

def create_tarefa_adapter(tarefa_data: CreateTarefasRequest, token: str):
    url = f"{settings.URL_API_SS}/v1/administrativo/tarefa"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    try:
        payload = tarefa_data.model_dump(mode="json")
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 404:
            logger.error("Supersapiens retornou 404. Verifique o endpoint ou os dados enviados.")
            return None

        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        logger.error(f"Erro ao criar tarefa: {str(e)}")
        return None
