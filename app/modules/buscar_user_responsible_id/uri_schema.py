from pydantic import BaseModel

class UserIDResponse(BaseModel):
    id: int