from fastapi import FastAPI
from starlette.responses import RedirectResponse

# Routers
from routes.ticket import ticket_router
from routes.event import event_router

from contextlib import asynccontextmanager
from database import EventoModel, TicketModel, database as connection

@asynccontextmanager
async def lifespan(app: FastAPI):

    if connection.is_closed():
        connection.connect()
    try:
        yield # Aqui se ejecuta la aplicacion
    finally:
        if not connection.is_closed:
            connection.close()



app = FastAPI(lifespan = lifespan)

# On Startup
#@app.on_event("startup")
#async def startup():
#    connection.connect()
    # Create tables if they do not exist
#    connection.create_tables([EventoModel, TicketModel])

# On Shutdown

# Documentacion
@app.get("/")
async def docs():
    return RedirectResponse(url= "/docs")


# Rutas
app.include_router(event_router, prefix= "/events", tags=["Events"])
app.include_router(ticket_router, prefix= "/tickets", tags=["Tickets"])