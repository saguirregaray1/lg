from fastapi import HTTPException
from pydantic import IPvAnyAddress

from app.db.devices import read_devices, read_devices_by_address


async def get_devices(ip_addr: IPvAnyAddress | None = None):
    if ip_addr:
        devices = read_devices_by_address(ip_addr)
    else:
        devices = read_devices(ip_addr)

    if not devices:
        raise HTTPException(
            status_code=404, detail="No commands found for the given platform"
        )
    return devices
