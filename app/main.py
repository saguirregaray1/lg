import jwt
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request

from app.core.config import settings

from .commands.router import router as commands_router
from .devices.router import router as devices_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def authenticate(request: Request, call_next):
    token = request.cookies.get("access_token", "")
    try:
        jwt.decode(token, settings.secret_key, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, "Expired token")
    except jwt.InvalidTokenError:
        raise HTTPException(401, "Invalid Token")

    response = await call_next(request)

    return response


app.include_router(devices_router, prefix="/devices")
app.include_router(commands_router, prefix="/commands")
