from pydantic import IPvAnyAddress

from app.core.config import settings
from ..schemas.devices import DevicesFile
from ..utils import read_yaml_file


def load_devices():
    devices_data = read_yaml_file(settings.devices_path, DevicesFile)

    devices = {}
    for device in devices_data.devices:
        devices[device.address] = device
    return devices


devices_db = load_devices()


def read_devices(ip_addr: IPvAnyAddress | None = None):
    if ip_addr:
        return devices_db.get(ip_addr)
    return devices_db


def read_devices_by_address(ip_addr: IPvAnyAddress):
    if ip_addr:
        return devices_db.get(ip_addr)
