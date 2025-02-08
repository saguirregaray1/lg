from commands.router import router as commands_router
from devices.router import router as devices_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(devices_router, prefix="/devices")
app.include_router(commands_router, prefix="/commands")
