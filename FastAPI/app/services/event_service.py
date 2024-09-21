"""
Service layer for Event operations.

This module contains the business logic for managing events.
It interacts with the EventoModel from the database and uses
the Event Pydantic model for data validation.
"""

from typing import Optional
from datetime import datetime
from peewee import DoesNotExist
from database import EventoModel
from models.event import Event


class EventService:
    """Service layer for Event operations."""

    @staticmethod
    def create_event(nombre: str, fecha: datetime, ubicacion: str) -> Event:
        """
        Create a new event.

        Args:
            name (str): The name of the event.
            date (str): The date of the event.
            location (str): The location of the event.

        Returns:
            Event: The created event instance as a Pydantic model.
        """
        event_instance = EventoModel.create(nombre=nombre, fecha=fecha, ubicacion=ubicacion)
        return Event(
            id=event_instance.id,
            nombre=event_instance.nombre,
            fecha=event_instance.fecha,
            ubicacion=event_instance.ubicacion,
        )

    @staticmethod
    def get_event_by_id(evento_id: int) -> Optional[Event]:
        """
        Retrieve an event by ID.

        Args:
            evento_id (int): The ID of the event to retrieve.

        Returns:
            Optional[Event]: The event instance as a Pydantic model if found, else None.
        """
        try:
            event_instance = EventoModel.get_by_id(evento_id)
            return Event(
                id=event_instance.id,
                nombre=event_instance.nombre,
                fecha=event_instance.fecha,
                ubicacion=event_instance.ubicacion,
            )
        except DoesNotExist:
            return None

    @staticmethod
    def update_event(
        evento_id: int, nombre: Optional[str] = None, fecha: Optional[datetime] = None,
          ubicacion: Optional[str] = None
    ) -> Optional[Event]:
        """
        Update an existing event by ID.

        Args:
            event_id (int): The ID of the event to update.
            nombre (Optional[str]): The new name of the event.
            fecha (Optional[datetime]): The new date of the event.
            ubicacion (Optional[str]): The new location of the event.

        Returns:
            Optional[Event]: The updated event instance as a Pydantic model if successful,
            else None.
        """
        try:
            event_instance = EventoModel.get_by_id(evento_id)
            if nombre:
                event_instance.nombre = nombre
            if fecha:
                event_instance.fecha = fecha
            if ubicacion:
                event_instance.ubicacion = ubicacion
            event_instance.save()  # Save changes to the database

            return Event(
                id=event_instance.id,
                name=event_instance.nombre,
                date=event_instance.fecha,
                location=event_instance.ubicacion,
            )
        except DoesNotExist:
            return None

    @staticmethod
    def delete_event(evento_id: int) -> bool:
        """
        Delete an event by ID.

        Args:
            evento_id (int): The ID of the event to delete.

        Returns:
            bool: True if the event was deleted, else False.
        """
        try:
            event_instance = EventoModel.get_by_id(evento_id)
            event_instance.delete_instance()
            return True
        except DoesNotExist:
            return False
