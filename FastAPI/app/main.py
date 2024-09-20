from fastapi import FastAPI
from starlette.responses import RedirectResponse

# Routers
from .routes.event import event_router
from .routes.ticket import ticket_router

from contextlib import asynccontextmanager
from database import database as connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    # COnectar a la base de datos si la conexcion esta cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield # Aqui se ejecuta la aplicacion
    finally:
        #  Cerrar la conexcion cuando la aplicacion se detenga
        if not connection.is_closed:
            connection.close()



app = FastAPI(lifespan = lifespan)

# On Startup
# On Shutdown

# Documentacion
@app.get("/")
async def docs():
    return RedirectResponse(url= "/docs")


# Rutas
app.include_router(event_router, prefix= "/events", tags=["Events"])
app.include_router(ticket_router, prefix= "/tickets", tags=["Tickets"])