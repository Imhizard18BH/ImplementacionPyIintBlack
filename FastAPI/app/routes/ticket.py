
"""
Module that defines the routes for managing tickets.

This module uses FastAPI to define the routes that allow
creating, reading, updating, and deleting tickets through a REST API.

Available routes:

- POST /tickets/: Creates a new ticket.
- GET /tickets/{ticket_id}: Retrieves ticket information by ID.
- PUT /tickets/{ticket_id}: Updates ticket information.
- DELETE /tickets/{ticket_id}: Deletes a ticket.

Each route uses the TicketService to interact with the
business logic related to tickets.
"""
from datetime import datetime
from services.ticket_service import TicketService
from models.ticket import Ticket
from fastapi import APIRouter, HTTPException


ticket_router = APIRouter()


@ticket_router.post("/tickets/", response_model=Ticket)
def create_ticket(evento_id: int, usuario_id: int, fecha_compra: str) -> Ticket:
    """
    Create a new ticket.

    Args:
        event_id (int): The ID of the associated event.
        user_id (int): The ID of the user purchasing the ticket.
        date_purchase (str): The purchase date of the ticket.

    Returns:
        Ticket: The created ticket.
    """
    ticket = TicketService.create_ticket(evento_id, usuario_id, fecha_compra)
    return ticket


@ticket_router.get("/tickets/{ticket_id}", response_model=Ticket)
def get_ticket(ticket_id: int) -> Ticket:
    """
    Retrieve ticket information by ID.

    Args:
        ticket_id (int): The ID of the ticket to retrieve.

    Returns:
        Ticket: The ticket with the specified ID.

    Raises:
        HTTPException: If the ticket is not found.
    """
    ticket = TicketService.get_ticket_by_id(ticket_id)
    if ticket:
        return ticket
    raise HTTPException(status_code=404, detail="Ticket not found")


@ticket_router.put("/tickets/{ticket_id}", response_model=Ticket)
def update_ticket(ticket_id: int, evento_id: int = None, usuario_id: int = None,
                  fecha_compra: datetime = None) -> Ticket:
    """
    Update ticket information.

    Args:
        ticket_id (int): The ID of the ticket to update.
        evento_id (int, optional): The new event ID associated with the ticket.
        usuario_id (int, optional): The new user ID purchasing the ticket.
        fecha_compra (datetime, optional): The new purchase date of the ticket.

    Returns:
        Ticket: The updated ticket.

    Raises:
        HTTPException: If the ticket is not found.
    """
    ticket = TicketService.update_ticket(ticket_id, evento_id, usuario_id, fecha_compra)
    if ticket:
        return ticket
    raise HTTPException(status_code=404, detail="Ticket not found")


@ticket_router.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int) -> dict:
    """
    Delete a ticket by ID.

    Args:
        ticket_id (int): The ID of the ticket to delete.

    Returns:
        dict: A confirmation message if the ticket was deleted.

    Raises:
        HTTPException: If the ticket is not found.
    """
    if TicketService.delete_ticket(ticket_id):
        return {"message": "Ticket deleted successfully"}
    raise HTTPException(status_code=404, detail="Ticket not found")
