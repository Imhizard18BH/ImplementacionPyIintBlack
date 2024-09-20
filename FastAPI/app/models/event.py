from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    id: int
    nombre: int
    fecha: datetime
    ubicacion: str