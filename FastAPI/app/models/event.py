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
        nombre (str): Name of the event.
        fecha (datetime): Date and time of the event.
        ubicacion (str): Location of the event.
    """
    id: int
    nombre: str
    fecha: datetime
    ubicacion: str
