"""
This module defines the Event class that represents an event with its ID, name, date, and location.
"""

from datetime import datetime
from pydantic import BaseModel


class Event(BaseModel):
    """
    Represents an event with ID, name, date, and location.

    Attributes:
        id (int): Unique identifier for the event.
        name (str): Name of the event.
        date (datetime): Date and time of the event.
        location (str): Location of the event.
    """

    id: int
    name: str
    date: datetime
    location: str
