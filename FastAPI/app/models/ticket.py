from pydantic import BaseModel
from datetime import datetime

class Ticket(BaseModel):
    id: int
    event_id: int
    user_id: int
    date_purchase: datetime

    