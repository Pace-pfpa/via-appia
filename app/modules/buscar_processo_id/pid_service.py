from app.modules.buscar_processo_id.pid_adapter import buscar_processo_id_adapter
from app.modules.buscar_processo_id.pid_schema import ProcessoIdResponse


def buscar_processo_id_service(nup:str, token: str) -> ProcessoIdResponse:
    processo_data = buscar_processo_id_adapter(nup, token)
    if processo_data:
        return ProcessoIdResponse(**processo_data)
    else:
        raise ValueError("Processo não encontrado")
