from fastapi import HTTPException

from app.core.config import settings
from ..schemas.devices import DevicesFile, IPv4WithPortModel
from ..utils import read_yaml_file


def load_devices():
    devices_data = read_yaml_file(settings.devices_path, DevicesFile)

    devices = {}
    for device in devices_data.devices:
        full_addr = f"{device.address}:{device.port}"
        if full_addr in devices:
            raise HTTPException(
                status_code=500,
                detail="Invalid devices file. Address + Port must be unique",
            )
        devices[full_addr] = device
    return devices


devices_db = load_devices()


def read_devices(ip_addr: IPv4WithPortModel | None = None):
    if ip_addr:
        return devices_db.get(ip_addr.address)
    return devices_db


def read_devices_by_address(ip_addr: IPv4WithPortModel):
    if ip_addr:
        return devices_db.get(ip_addr.address)
