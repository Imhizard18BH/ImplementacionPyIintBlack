"""
Module that defines the routes for managing events.

This module uses FastAPI to define the routes that allow
creating, reading, updating, and deleting events through a REST API.

Available routes:

- POST /events/: Creates a new event.
- GET /events/{event_id}: Retrieves event information by ID.
- PUT /events/{event_id}: Updates event information.
- DELETE /events/{event_id}: Deletes an event.

Each route uses the EventService to interact with the
business logic related to events.
"""

from datetime import datetime
from services.event_service import EventService
from models.event import Event
from fastapi import APIRouter, HTTPException


event_router = APIRouter()


@event_router.post("/events/", response_model=Event)
def create_event(name: str, date: str, location: str) -> Event:
    """
    Create a new event.

    Args:
        name (str): The name of the event.
        date (str): The date of the event.
        location (str): The location of the event.

    Returns:
        Event: The created event.
    """
    event = EventService.create_event(name, date, location)
    return event


@event_router.get("/events/{event_id}", response_model=Event)
def get_event(event_id: int) -> Event:
    """
    Retrieve event information by ID.

    Args:
        event_id (int): The ID of the event to retrieve.

    Returns:
        Event: The event with the specified ID.

    Raises:
        HTTPException: If the event is not found.
    """
    event = EventService.get_event_by_id(event_id)
    if event:
        return event
    raise HTTPException(status_code=404, detail="Event not found")


@event_router.put("/events/{event_id}", response_model=Event)
def update_event(
    event_id: int, name: str = None, date: datetime = None, location: str = None
) -> Event:
    """
    Update event information.

    Args:
        event_id (int): The ID of the event to update.
        name (str, optional): The new name of the event.
        date (datetime, optional): The new date of the event.
        location (str, optional): The new location of the event.

    Returns:
        Event: The updated event.

    Raises:
        HTTPException: If the event is not found.
    """
    event = EventService.update_event(event_id, name, date, location)
    if event:
        return event
    raise HTTPException(status_code=404, detail="Event not found")


@event_router.delete("/events/{event_id}")
def delete_event(event_id: int) -> dict:
    """
    Delete an event by ID.

    Args:
        event_id (int): The ID of the event to delete.

    Returns:
        dict: A confirmation message if the event was deleted.

    Raises:
        HTTPException: If the event is not found.
    """
    if EventService.delete_event(event_id):
        return {"message": "Event deleted successfully"}
    raise HTTPException(status_code=404, detail="Event not found")
