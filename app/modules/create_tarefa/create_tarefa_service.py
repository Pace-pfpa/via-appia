from app.modules.create_tarefa.create_tarefa_adapter import create_tarefa_adapter
from app.modules.create_tarefa.create_tarefa_schema import CreateTarefaRequest, CreateTarefaSupersapiensResponse
from app.core.logger import logger
import json

def create_tarefa_service(tarefa_data: CreateTarefaRequest, token: str) -> CreateTarefaSupersapiensResponse:
    try:
        resposta_supersapiens = create_tarefa_adapter(tarefa_data, token)
        logger.info(f"Resposta da Supersapiens: {json.dumps(resposta_supersapiens, indent=2)}")
        return CreateTarefaSupersapiensResponse(**resposta_supersapiens)
    except Exception as e:
        raise Exception(f"Erro no serviço de criação de tarefa: {str(e)}")