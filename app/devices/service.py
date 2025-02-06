from fastapi import HTTPException

from app.devices.db import read_devices, read_devices_by_address
from app.devices.schema import IPv4WithPortModel


async def get_devices(ip_addr: IPv4WithPortModel | None = None):
    if ip_addr:
        devices = read_devices_by_address(ip_addr)
    else:
        devices = read_devices(ip_addr)

    if not devices:
        raise HTTPException(
            status_code=404, detail="No commands found for the given platform"
        )
    return devices
