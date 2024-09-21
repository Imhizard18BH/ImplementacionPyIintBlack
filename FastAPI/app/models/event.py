from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    id: int
    name: int
    date: datetime
    location: str