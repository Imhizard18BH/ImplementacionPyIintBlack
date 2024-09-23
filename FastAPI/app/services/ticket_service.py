"""
Service layer for Ticket operations.

This module contains the business logic for managing tickets.
It interacts with the TicketModel from the database and uses
the Ticket Pydantic model for data validation.
"""

from typing import Optional
from datetime import datetime
from peewee import DoesNotExist
from database import TicketModel
from models.ticket import Ticket


class TicketService:
    """Service layer for Ticket operations."""

    @staticmethod
    def create_ticket(
        evento_id: int, usuario_id: int, fecha_compra: datetime
    ) -> Ticket:
        """
        Create a new ticket.

        Args:
            evento_id (int): The ID of the associated event.
            usuario_id (int): The ID of the user purchasing the ticket.
            fecha_compra (datetime): The purchase date of the ticket.

        Returns:
            Ticket: The created ticket instance as a Pydantic model.
        """
        ticket_instance = TicketModel.create(
            evento_id=evento_id, usuario_id=usuario_id, fecha_compra=fecha_compra
        )
        return Ticket(
            id=ticket_instance.id,
            evento_id=ticket_instance.evento_id,
            usuario_id=ticket_instance.usuario_id,
            fecha_compra=ticket_instance.fecha_compra,
        )

    @staticmethod
    def get_ticket_by_id(ticket_id: int) -> Optional[Ticket]:
        """
        Retrieve a ticket by ID.

        Args:
            ticket_id (int): The ID of the ticket to retrieve.

        Returns:
            Optional[Ticket]: The ticket instance as a Pydantic model if found, else None.
        """
        try:
            ticket_instance = TicketModel.get_by_id(ticket_id)
            return Ticket(
                id=ticket_instance.id,
                evento_id=ticket_instance.evento_id.id,
                usuario_id=ticket_instance.usuario_id,
                fecha_compra=ticket_instance.fecha_compra,
            )
        except DoesNotExist:
            return None

    @staticmethod
    def update_ticket(
        ticket_id: int,
        evento_id: Optional[int] = None,
        usuario_id: Optional[int] = None,
        fecha_compra: Optional[datetime] = None,
    ) -> Optional[Ticket]:
        """
        Update an existing ticket by ID.

        Args:
            ticket_id (int): The ID of the ticket to update.
            evento_id (Optional[int]): The new event ID associated with the ticket.
            usuario_id (Optional[int]): The new user ID purchasing the ticket.
            fecha_compra (Optional[datetime]): The new purchase date of the ticket.

        Returns:
            Optional[Ticket]: The updated ticket instance as a Pydantic model if successful,
            else None.
        """
        try:
            ticket_instance = TicketModel.get_by_id(ticket_id)
            if evento_id is not None:
                ticket_instance.evento_id = evento_id
            if usuario_id is not None:
                ticket_instance.usuario_id = usuario_id
            if fecha_compra:
                ticket_instance.fecha_compra = fecha_compra
            ticket_instance.save()  # Save changes to the database

            return Ticket(
                id=ticket_instance.id,
                evento_id=ticket_instance.evento_id.id,
                usuario_id=ticket_instance.usuario_id,
                fecha_compra=ticket_instance.fecha_compra,
            )
        except DoesNotExist:
            return None

    @staticmethod
    def delete_ticket(ticket_id: int) -> bool:
        """
        Delete a ticket by ID.

        Args:
            ticket_id (int): The ID of the ticket to delete.

        Returns:
            bool: True if the ticket was deleted, else False.
        """
        try:
            ticket_instance = TicketModel.get_by_id(ticket_id)
            ticket_instance.delete_instance()
            return True
        except DoesNotExist:
            return False
