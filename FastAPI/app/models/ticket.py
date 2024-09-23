"""
This module defines the Ticket class that represents a ticket with its ID, event_id,
user_id, and purchase_date.
"""

from datetime import datetime
from pydantic import BaseModel


class Ticket(BaseModel):
    """
    Class representing a Ticket.

    Attributes:
        id (int): Unique identifier for the ticket.
        evento_id (int): Identifier for the associated event.
        usuario_id (int): Identifier for the user who purchased the ticket.
        fecha_compra (datetime): Date and time of the ticket purchase.
    """

    id: int
    evento_id: int
    usuario_id: int
    fecha_compra: datetime
