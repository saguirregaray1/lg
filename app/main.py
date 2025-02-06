from fastapi import FastAPI

app = FastAPI()

app.include_router(devices.router, prefix="/devices")
app.include_router(commands.router, prefix="/commands")
