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
        event_id (int): Identifier for the associated event.
        user_id (int): Identifier for the user who purchased the ticket.
        purchase_date (datetime): Date and time of the ticket purchase.
    """

    id: int
    event_id: int
    user_id: int
    purchase_date: datetime
