from fastapi import APIRouter, Body
from FastAPI.app.models.ticket import Ticket
from FastAPI.app.database import TicketModel
from datetime import datetime

ticket_router = APIRouter()

@ticket_router.get("/tickets")
def get_tickets():

    try:
        tickets = TicketModel.select().where(TicketModel.id > 0).dicts()
        if tickets:
            return list(tickets)
    except TicketModel.DoesNotExist:
        return "No tickets found"
    
@ticket_router.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    try:
        ticket = TicketModel.get(TicketModel.id == ticket_id)
        return ticket
    except TicketModel.DoesNotExist:
        return "ticket not found"
    
@ticket_router.post("/tickets")
def create_ticket(ticket: Ticket = Body(...)):
    ticket = TicketModel.create(evento_id=ticket.evento_id, usuario_id=ticket.usuario_id, fecha_compra=ticket.fecha_compra)
    return ticket

@ticket_router.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, ticket_data: dict):
    TicketModel.update(**ticket_data).where(TicketModel.id == ticket_id).execute()
    ticket = TicketModel.get(TicketModel.id == ticket_id)
    return ticket

@ticket_router.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    try:
        ticket = TicketModel.get(TicketModel.id == ticket_id)
        if ticket:
            ticket.delete_instance()
            return {"message": "ticket deleted successfully"}
        else:
            raise TicketModel.DoesNotExist(status_code=404, detail="ticket not found")
    except TicketModel.DoesNotExist:
        return "ticket not found"

