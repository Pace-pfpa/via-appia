from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime

class CreateTarefasRequest(BaseModel):
    bloco: bool = True
    blocoProcessos: bool = True
    blocoResponsaveis: Optional[str] = None
    dataHoraDistribuicao: Optional[datetime] = None
    dataHoraFinalPrazo: Optional[datetime] = None
    dataHoraInicioPrazo: datetime = None
    dataHoraLeitura: Optional[datetime] = None
    diasUteis: Optional[int] = None
    distribuicaoAutomatica: Optional[bool] = None
    especieTarefa: int
    folder: Optional[str] = None
    grupoContato: Optional[int] = None
    isRelevante: Optional[bool] = None
    localEvento: Optional[str] = None
    locked: Optional[bool] = None
    observacao: str
    postIt: Optional[str] = None
    prazoDias: int
    processo: int
    processos: Optional[int] = None
    setorOrigem: int
    setorResponsavel: int
    setores: Optional[int] = None
    urgente: Optional[bool] = None
    usuarioResponsavel: int
    usuarios: Optional[int] = None

class CreateTarefasRequestNewPace(BaseModel):
    id_av: int
    data: datetime
    id_especie: int
    id_setor: int
    aud: List[str]
    obs: str

class CreateTarefasSupersapiensResponse(BaseModel):
    tarefas_sucesso: Dict[str, Optional[int | str]]
    tarefas_fracasso: Dict[str, str]
