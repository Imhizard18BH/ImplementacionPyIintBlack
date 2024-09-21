from FastAPI import APIRouter, HTTPException, Body
from FastAPI.app.models.ticket import Ticket
from FastAPI.app.database import TicketModel
from datetime import datetime

ticket_router = APIRouter()

# GET /tickets - Retrieve all tickets
@ticket_router.get("/tickets", response_model=list[Ticket])
def get_tickets():
    try:
        tickets = TicketModel.select().where(TicketModel.id > 0).dicts()
        if tickets:
            return list(tickets)
        else:
            raise HTTPException(status_code=404, detail="No tickets found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET /tickets/{ticket_id} - Retrieve a ticket by ID
@ticket_router.get("/tickets/{ticket_id}", response_model=Ticket)
def get_ticket(ticket_id: int):
    try:
        ticket = TicketModel.get(TicketModel.id == ticket_id)
        return ticket
    except TicketModel.DoesNotExist:
        raise HTTPException(status_code=404, detail="Ticket not found")

# POST /tickets - Create a new ticket
@ticket_router.post("/tickets", response_model=Ticket)
def create_ticket(ticket: Ticket = Body(...)):
    try:
        new_ticket = TicketModel.create(
            evento_id=ticket.evento_id, 
            usuario_id=ticket.usuario_id, 
            fecha_compra=ticket.fecha_compra or datetime.now()
        )
        return new_ticket
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# PUT /tickets/{ticket_id} - Update a ticket by ID
@ticket_router.put("/tickets/{ticket_id}", response_model=Ticket)
def update_ticket(ticket_id: int, ticket_data: dict = Body(...)):
    try:
        rows_updated = TicketModel.update(**ticket_data).where(TicketModel.id == ticket_id).execute()

        if rows_updated == 0:
            raise HTTPException(status_code=404, detail="Ticket not found")
        
        updated_ticket = TicketModel.get(TicketModel.id == ticket_id)
        return updated_ticket
    except TicketModel.DoesNotExist:
        raise HTTPException(status_code=404, detail="Ticket not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# DELETE /tickets/{ticket_id} - Delete a ticket by ID
@ticket_router.delete("/tickets/{ticket_id}", response_model=dict)
def delete_ticket(ticket_id: int):
    try:
        ticket = TicketModel.get(TicketModel.id == ticket_id)
        ticket.delete_instance()
        return {"message": "Ticket deleted successfully"}
    except TicketModel.DoesNotExist:
        raise HTTPException(status_code=404, detail="Ticket not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
