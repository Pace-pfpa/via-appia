from pydantic import BaseModel

class BuscarTarefaRequest(BaseModel):
    idTarefa: int

class BuscarTarefaResponse(BaseModel):
    id: int
