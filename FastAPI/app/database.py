"""
Module for database configuration and models.
"""

import os
from dotenv import load_dotenv
from peewee import MySQLDatabase, Model, AutoField, CharField
from peewee import DateTimeField, ForeignKeyField, IntegerField


# Cargar variables de entorno desde el archivo .env
load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class EventoModel(Model):
    """
    Class representing the event model.

    Attributes:
        id (int): Unique identifier for the event.
        name (str): Name of the event.
        date (datetime): Date and time of the event.
        location (str): Location of the event.
    """

    id = AutoField(primary_key=True)
    nombre = CharField(max_length=50)
    fecha = DateTimeField()
    ubicacion = CharField(max_length=50)

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Configuration for the EventoModel class.

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
        evento_id (int): Identifier for the associated event.
        usuario_id (int): Identifier for the user who purchased the ticket.
        fecha_compra (datetime): Date and time of the ticket purchase.
    """

    id = AutoField(primary_key=True)
    evento_id = ForeignKeyField(EventoModel, backref="tickets")
    usuario_id = IntegerField()
    fecha_compra = DateTimeField()

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Configuration for the TicketModel class.

        Attributes:
            database: Database used.
            table_name: Name of the table in the database.
        """

        database = database
        table_name = "tickets"
