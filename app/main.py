from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .commands.router import router as commands_router
from .devices.router import router as devices_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(devices_router, prefix="/devices")
app.include_router(commands_router, prefix="/commands")
