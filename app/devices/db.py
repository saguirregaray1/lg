from fastapi import HTTPException

from app.core.config import settings
from app.devices.schema import Device, DevicesFile, IPWithPortModel
from app.utils import read_yaml_file


def load_devices() -> dict[str, Device]:
    devices_data = read_yaml_file(settings.config_path / "devices.yaml", DevicesFile)

    devices: dict[str, Device] = {}
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


def read_devices() -> dict[str, Device] | None:
    return devices_db


def read_devices_by_address(ip_addr: IPWithPortModel) -> Device | None:
    full_addr = f"{ip_addr.address}:{ip_addr.port}"
    return devices_db.get(full_addr)
