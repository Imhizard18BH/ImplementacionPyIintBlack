"""
Main module for the FastAPI application.

This module creates and configures the FastAPI application instance,
registers routers for different routes, and includes the API documentation.
"""

from app.routes import event_router
from app.routes import ticket_router
from fastapi import FastAPI


app = FastAPI()

# Register the routers with prefixes
app.include_router(event_router, prefix="/api/events")
app.include_router(ticket_router, prefix="/api/tickets")
