from app.modules.create_tarefas.create_tarefas_adapter import create_tarefa_adapter
from app.modules.create_tarefas.create_tarefas_schema import CreateTarefasRequestNewPace, CreateTarefasRequest, CreateTarefasSupersapiensResponse
from datetime import datetime, timedelta

def calcular_prazo_final(data_inicio: datetime, dias: int) -> datetime:
    return data_inicio + timedelta(days=dias)

def validar_processo_id(processo_id: str) -> bool:
    return processo_id.isdigit() and len(processo_id) == 8

def create_tarefas_service(request_data: CreateTarefasRequestNewPace, token: str) -> CreateTarefasSupersapiensResponse:
    tarefas_sucesso = {}
    tarefas_fracasso = {}

    for processo_id in request_data.aud:
        if not validar_processo_id(processo_id):
            tarefas_fracasso[processo_id] = "ID de processo inválido"
            continue

        data_final_prazo = calcular_prazo_final(request_data.data, 5)

        tarefa_data = CreateTarefasRequest(
            bloco=True,
            blocoProcessos=True,
            dataHoraInicioPrazo=request_data.data,
            dataHoraFinalPrazo= data_final_prazo,
            especieTarefa=request_data.id_especie,
            observacao=request_data.obs,
            prazoDias=5,
            processo=int(processo_id),
            setorOrigem=request_data.id_setor,
            setorResponsavel=request_data.id_setor,
            usuarioResponsavel=request_data.id_av
        )

        resposta = create_tarefa_adapter(tarefa_data, token)

        if resposta and "@id" in resposta:
            id_tarefa = int(resposta["@id"].split("/")[-1])
            tarefas_sucesso[processo_id] = id_tarefa
        else:
            tarefas_fracasso[processo_id] = "Erro ao criar tarefa"

    return CreateTarefasSupersapiensResponse(
        tarefas_sucesso=tarefas_sucesso,
        tarefas_fracasso=tarefas_fracasso
    )
