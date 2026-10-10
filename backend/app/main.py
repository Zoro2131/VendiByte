#imports
from fastapi import FastAPI
from app.api.v1 import machines


# instance creation 
app = FastAPI(title="VendiStep API")


# Router Designation 
app.include_router(machines.router, prefix="/api/v1")