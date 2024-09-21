from dotenv import load_dotenv
from peewee import *


import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)

class EventoModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    date = DateTimeField()
    location = CharField(max_length=50) 

    class Meta:
        database = database
        table_name = "events"

class TicketModel(Model):
    id = AutoField(primary_key=True)
    event_id = ForeignKeyField(EventoModel, backref="tickets")
    user_id = IntegerField()
    date_purchase = DateTimeField()

    class Meta:
        database = database
        table_name = "tickets"

