from fastapi import APIRouter, Body
from FastAPI.app.models.event import Event
from database import EventoModel

event_router = APIRouter()

@event_router.get("/events")
def get_events():

    try:
        events = EventoModel.select().where(EventoModel.id > 0).dicts()
        if events:
            return list(events)
    except EventoModel.DoesNotExist:
        return "No events found"
    
@event_router.get("/events/{event_id}")
def get_event(event_id: int):
    try:
        event = EventoModel.get(EventoModel.id == event_id)
        return event
    except EventoModel.DoesNotExist:
        return "Event not found"
    
@event_router.post("/events")
def create_event(event: Event = Body(...)):
    event = EventoModel.create(nombre=event.nombre, fecha=event.fecha, ubicacion=event.ubicacion)
    return event

@event_router.put("/events/{event_id}")
def update_event(event_id: int, event_data: dict):
    EventoModel.update(**event_data).where(EventoModel.id == event_id).execute()
    event = EventoModel.get(EventoModel.id == event_id)
    return event

@event_router.delete("/events/{event_id}")
def delete_event(event_id: int):
    try:
        event = EventoModel.get(EventoModel.id == event_id)
        if event:
            event.delete_instance()
            return {"message": "Event deleted successfully"}
        else:
            raise EventoModel.DoesNotExist(status_code=404, detail="Event not found")
    except EventoModel.DoesNotExist:
        return "Event not found"

