from pydantic import BaseModel
from typing import Optional

class UserQuery(BaseModel):
    message: str

class BotResponse(BaseModel):
    response: str
    severity:  Optional[str] = None
