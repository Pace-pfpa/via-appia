import requests
from app.core.settings import settings
from app.core.logger import logger
from app.modules.buscar_tarefa.buscar_tarefa_schema import BuscarTarefaResponse


def buscar_tarefa(idTarefa: int, token: str) -> BuscarTarefaResponse:
    url = f"{settings.URL_API_SS}/v1/administrativo/tarefa/{idTarefa} "
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.request("GET", url, headers=headers)
        tarefa = response.json()
        return tarefa

    except requests.RequestException as e:
        logger.error(f"Erro ao buscar tarefas: {str(e)}")
        raise Exception(f"Erro ao buscar tarefas: {str(e)}")