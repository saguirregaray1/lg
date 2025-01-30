from fastapi import APIRouter
from pydantic import IPvAnyAddress

from app.services.devices import get_devices


router = APIRouter()


@router.get("/")
async def read_devices(ip_addr: IPvAnyAddress | None = None):
    return await get_devices(ip_addr)
