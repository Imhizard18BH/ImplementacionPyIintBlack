from pydantic import BaseModel
from datetime import datetime

class Ticket(BaseModel):
    id: int
    evento_id: int
    usuario_id: int
    fecha_compra: datetime

    