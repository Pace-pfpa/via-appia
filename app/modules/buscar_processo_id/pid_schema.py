from pydantic import BaseModel

class ProcessoIdRequest(BaseModel):
    nup: str

class ProcessoIdResponse(BaseModel):
    processoId: str
    nup: str