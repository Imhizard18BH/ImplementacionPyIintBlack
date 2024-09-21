from FastAPI import APIRouter, HTTPException, Body
from FastAPI.app.models.event import Event
from database import EventoModel 

event_router = APIRouter()

# GET /events - Retrieve all events
@event_router.get("/events", response_model=list[Event])
def get_events():
    try:
        events = EventoModel.select().where(EventoModel.id > 0).dicts()
        if events:
            return list(events)
        else:
            raise HTTPException(status_code=404, detail="No events found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# GET /events/{event_id} - Retrieve an event by ID
@event_router.get("/events/{event_id}", response_model=Event)
def get_event(event_id: int):
    try:
        event = EventoModel.get(EventoModel.id == event_id)
        return event
    except EventoModel.DoesNotExist:
        raise HTTPException(status_code=404, detail="Event not found")

# POST /events - Create a new event
@event_router.post("/events", response_model=Event)
def create_event(event: Event = Body(...)):
    try:
        new_event = EventoModel.create(
            nombre=event.nombre, 
            fecha=event.fecha, 
            ubicacion=event.ubicacion
        )
        return new_event
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# PUT /events/{event_id} - Update an event by ID
@event_router.put("/events/{event_id}", response_model=Event)
def update_event(event_id: int, event_data: dict = Body(...)):
    try:
        # Update the event with the received data
        rows_updated = EventoModel.update(**event_data).where(EventoModel.id == event_id).execute()
        
        if rows_updated == 0:
            raise HTTPException(status_code=404, detail="Event not found")
        
        # Return the updated event
        updated_event = EventoModel.get(EventoModel.id == event_id)
        return updated_event
    except EventoModel.DoesNotExist:
        raise HTTPException(status_code=404, detail="Event not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# DELETE /events/{event_id} - Delete an event by ID
@event_router.delete("/events/{event_id}", response_model=dict)
def delete_event(event_id: int):
    try:
        event = EventoModel.get(EventoModel.id == event_id)
        event.delete_instance()
        return {"message": "Event deleted successfully"}
    except EventoModel.DoesNotExist:
        raise HTTPException(status_code=404, detail="Event not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
