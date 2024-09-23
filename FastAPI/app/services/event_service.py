"""
Service layer for Event operations.

This module contains the business logic for managing events.
It interacts with the EventModel from the database and uses
the Event Pydantic model for data validation.
"""

from typing import Optional
from datetime import datetime
from peewee import DoesNotExist
from database import EventModel
from models.event import Event


class EventService:
    """Service layer for Event operations."""

    @staticmethod
    def create_event(name: str, date: datetime, location: str) -> Event:
        """
        Create a new event.

        Args:
            name (str): The name of the event.
            date (datetime): The date of the event.
            location (str): The location of the event.

        Returns:
            Event: The created event instance as a Pydantic model.
        """
        event_instance = EventModel.create(
            name=name, date=date, location=location
        )
        return Event(
            id=event_instance.id,
            name=event_instance.name,
            date=event_instance.date,
            location=event_instance.location,
        )

    @staticmethod
    def get_event_by_id(event_id: int) -> Optional[Event]:
        """
        Retrieve an event by ID.

        Args:
            event_id (int): The ID of the event to retrieve.

        Returns:
            Optional[Event]: The event instance as a Pydantic model if found, else None.
        """
        try:
            event_instance = EventModel.get_by_id(event_id)
            return Event(
                id=event_instance.id,
                name=event_instance.name,
                date=event_instance.date,
                location=event_instance.location,
            )
        except DoesNotExist:
            return None

    @staticmethod
    def update_event(
        event_id: int,
        name: Optional[str] = None,
        date: Optional[datetime] = None,
        location: Optional[str] = None,
    ) -> Optional[Event]:
        """
        Update an existing event by ID.

        Args:
            event_id (int): The ID of the event to update.
            name (Optional[str]): The new name of the event.
            date (Optional[datetime]): The new date of the event.
            location (Optional[str]): The new location of the event.

        Returns:
            Optional[Event]: The updated event instance as a Pydantic model if successful,
            else None.
        """
        try:
            event_instance = EventModel.get_by_id(event_id)
            if name:
                event_instance.name = name
            if date:
                event_instance.date = date
            if location:
                event_instance.location = location
            event_instance.save()  # Save changes to the database

            return Event(
                id=event_instance.id,
                name=event_instance.name,
                date=event_instance.date,
                location=event_instance.location,
            )
        except DoesNotExist:
            return None

    @staticmethod
    def delete_event(event_id: int) -> bool:
        """
        Delete an event by ID.

        Args:
            event_id (int): The ID of the event to delete.

        Returns:
            bool: True if the event was deleted, else False.
        """
        try:
            event_instance = EventModel.get_by_id(event_id)
            event_instance.delete_instance()
            return True
        except DoesNotExist:
            return False
