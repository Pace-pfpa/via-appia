import requests
import re
import json
from app.core.settings import settings

CNJ_REGEX = re.compile(r'^\d{7}-\d{2}\.\d{4}\.\d{1,2}\.\d{2}\.\d{4}$|^\d{20}$')

def validar_cnj(num_processo: str) -> bool:
    return bool(CNJ_REGEX.match(num_processo))

def formatar_cnj(num_processo: str) -> str:
    return re.sub(r'\D', '', num_processo) + "%"

def buscar_processos_id_adapter(num_processo: str, token: str):
    if not validar_cnj(num_processo):
        return None

    url = f"{settings.URL_API_SS}/v1/administrativo/processo"
    cnj_formatado = formatar_cnj(num_processo)

    where_clause = {
        "andX": [
            {"vinculacoesProcessosJudiciaisProcessos.processoJudicial.numero": f"like:{cnj_formatado}"}
        ]
    }

    query_params = {
        "where": json.dumps(where_clause, ensure_ascii=False),
        "limit": 30,
        "offset": 0,
        "order": json.dumps({}),
        "populate": json.dumps([
            "especieProcesso",
            "especieProcesso.generoProcesso",
            "setorAtual",
            "setorAtual.unidade"
        ]),
        "context": json.dumps({"modulo": "administrativo"})
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, params=query_params, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()

        if not data.get("entities"):
            return None

        processo_id = data["entities"][0].get("@id", "")
        return processo_id.split("/")[-1] if processo_id else None

    except requests.Timeout:
        return None

    except requests.RequestException:
        return None
