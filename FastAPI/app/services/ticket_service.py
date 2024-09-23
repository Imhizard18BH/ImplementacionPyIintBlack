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
        event_id: int, user_id: int, purchase_date: datetime
    ) -> Ticket:
        """
        Create a new ticket.

        Args:
            event_id (int): The ID of the associated event.
            user_id (int): The ID of the user purchasing the ticket.
            purchase_date (datetime): The purchase date of the ticket.

        Returns:
            Ticket: The created ticket instance as a Pydantic model.
        """
        ticket_instance = TicketModel.create(
            event_id=event_id, user_id=user_id, purchase_date=purchase_date
        )
        return Ticket(
            id=ticket_instance.id,
            event_id=ticket_instance.event_id.id,
            user_id=ticket_instance.user_id,
            purchase_date=ticket_instance.purchase_date,
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
                event_id=ticket_instance.event_id.id,
                user_id=ticket_instance.user_id,
                purchase_date=ticket_instance.purchase_date,
            )
        except DoesNotExist:
            return None

    @staticmethod
    def update_ticket(
        ticket_id: int,
        event_id: Optional[int] = None,
        user_id: Optional[int] = None,
        purchase_date: Optional[datetime] = None,
    ) -> Optional[Ticket]:
        """
        Update an existing ticket by ID.

        Args:
            ticket_id (int): The ID of the ticket to update.
            event_id (Optional[int]): The new event ID associated with the ticket.
            user_id (Optional[int]): The new user ID purchasing the ticket.
            purchase_date (Optional[datetime]): The new purchase date of the ticket.

        Returns:
            Optional[Ticket]: The updated ticket instance as a Pydantic model if successful,
            else None.
        """
        try:
            ticket_instance = TicketModel.get_by_id(ticket_id)
            if event_id is not None:
                ticket_instance.event_id = event_id
            if user_id is not None:
                ticket_instance.user_id = user_id
            if purchase_date:
                ticket_instance.purchase_date = purchase_date
            ticket_instance.save()  # Save changes to the database

            return Ticket(
                id=ticket_instance.id,
                event_id=ticket_instance.event_id.id,
                user_id=ticket_instance.user_id,
                purchase_date=ticket_instance.purchase_date,
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
