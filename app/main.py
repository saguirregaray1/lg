from fastapi import FastAPI
from .routers import devices, commands

app = FastAPI()

app.include_router(devices.router, prefix="/devices")
app.include_router(commands.router, prefix="/commands")
