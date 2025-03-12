from app.modules.buscar_processos_id.pid_adapter import buscar_processos_id_adapter
from app.modules.buscar_processos_id.pid_schema import ProcessosIdResponse

def buscar_processos_id_service(numeros_processos: list[str], token: str) -> ProcessosIdResponse:
    resultados = []

    for num_processo in numeros_processos:
        processo_id = buscar_processos_id_adapter(num_processo, token)
        resultados.append(processo_id)

    return ProcessosIdResponse(processos=resultados)

