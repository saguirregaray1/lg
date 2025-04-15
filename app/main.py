from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .commands.router import router as commands_router
from .devices.router import router as devices_router

# app = FastAPI(dependencies=[Depends(authenticate)])
app = FastAPI()

origins = ["http://localhost:8002", "http://localhost:8003", "http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(devices_router, prefix="/devices")
app.include_router(commands_router, prefix="/commands")
