from typing import Dict, List, Optional
from pydantic import BaseModel

class ProcessosIdRequest(BaseModel):
    numeros_processos: List[str]

class ProcessosIdResponse(BaseModel):
    processos: Dict[str, Optional[int | str]]