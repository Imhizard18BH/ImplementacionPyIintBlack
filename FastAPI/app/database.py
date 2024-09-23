"""
Module for database configuration and models.
"""

import os
from dotenv import load_dotenv
from peewee import MySQLDatabase, Model, AutoField, CharField
from peewee import DateTimeField, ForeignKeyField, IntegerField


# Load environment variables from the .env file
load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class EventModel(Model):
    """
    Class representing the event model.

    Attributes:
        id (int): Unique identifier for the event.
        name (str): Name of the event.
        date (datetime): Date and time of the event.
        location (str): Location of the event.
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    date = DateTimeField()
    location = CharField(max_length=50)

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Configuration for the EventModel class.

        Attributes:
            database: Database used.
            table_name: Name of the table in the database.
        """

        database = database
        table_name = "events"


class TicketModel(Model):
    """
    Class representing the ticket model.

    Attributes:
        id (int): Unique identifier for the ticket.
        event_id (int): Identifier for the associated event.
        user_id (int): Identifier for the user who purchased the ticket.
        purchase_date (datetime): Date and time of the ticket purchase.
    """

    id = AutoField(primary_key=True)
    event_id = ForeignKeyField(EventModel, backref="tickets")
    user_id = IntegerField()
    purchase_date = DateTimeField()

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Configuration for the TicketModel class.

        Attributes:
            database: Database used.
            table_name: Name of the table in the database.
        """

        database = database
        table_name = "tickets"
