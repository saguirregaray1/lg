from fastapi import APIRouter

from app.core.config import settings
from app.schemas.devices import DevicesFile

from app.utils import read_yaml_file

router = APIRouter()


@router.get("/")
async def read_devices():
    devices_file = read_yaml_file(settings.devices_path, DevicesFile)
    return devices_file.devices
