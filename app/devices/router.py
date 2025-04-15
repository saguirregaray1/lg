from typing import Annotated

from fastapi import APIRouter, HTTPException, Path
from fastapi.params import Depends
from pydantic import ValidationError
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from app.devices.schema import DeviceResponse, IPWithPortModel
from app.devices.service import get_device_by_ip, get_devices


def parse_ip_with_port(ip_addr: str = Path(...)) -> IPWithPortModel:
    try:
        ip, port = ip_addr.rsplit(":", 1)
        return IPWithPortModel(address=ip, port=int(port))
    except (ValueError, ValidationError):
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid format. Expected format: <ip>:<port>",
        )


router = APIRouter()


@router.get("/", response_model=list[DeviceResponse])
async def read_devices() -> list[DeviceResponse]:
    devices = await get_devices()
    return [DeviceResponse(**d.model_dump()) for d in devices.values()]


@router.get("/by-address", response_model=DeviceResponse)
async def read_device(
    ip: Annotated[IPWithPortModel, Depends()],
) -> DeviceResponse:
    device = await get_device_by_ip(ip)
    return DeviceResponse(**device.model_dump())
