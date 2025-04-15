from fastapi import HTTPException

from app.devices.db import read_devices, read_devices_by_address
from app.devices.schema import Device, IPWithPortModel


async def get_devices() -> dict[str, Device]:
    devices = read_devices()

    if not devices:
        raise HTTPException(status_code=404, detail="No devices found")

    return devices


async def get_device_by_ip(ip_addr: IPWithPortModel) -> Device:
    device = read_devices_by_address(ip_addr)

    if device is None:
        raise HTTPException(
            status_code=404, detail="No device found for the given IP Address"
        )

    return device
