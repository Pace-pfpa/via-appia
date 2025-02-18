from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreateTarefaSupersapiensResponse(BaseModel):
    id: int
    uuid: str
    observacao: str
    urgente: bool
    dataHoraInicioPrazo: datetime
    dataHoraFinalPrazo: datetime
    locked: bool
    dataHoraDistribuicao: Optional[datetime] = None
    redistribuida: bool
    distribuicaoAutomatica: bool
    livreBalanceamento: bool
    tipoDistribuicao: int
    isRelevante: bool
    criadoEm: datetime
    atualizadoEm: datetime

class CreateTarefaRequest(BaseModel):
    bloco: Optional[bool] = None
    blocoProcessos: Optional[bool] = None
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
