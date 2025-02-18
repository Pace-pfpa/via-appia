from app.modules.buscar_tarefa.buscar_tarefa_adapter import buscar_tarefa
from app.modules.buscar_tarefa.buscar_tarefa_schema import BuscarTarefaResponse


def buscar_tarefa_service(idTarefa: int, token: str) -> BuscarTarefaResponse:
    if not token:
        raise Exception("Token de autenticação inválido ou ausente.")

    return buscar_tarefa(idTarefa, token)