from enum import Enum
from typing import List

from pydantic import BaseModel, IPvAnyAddress, conint


class Platform(str, Enum):
    cisco_ios = "cisco_ios"
    cisco_xr = "cisco_xr"
    juniper = "juniper"
    frr = "frrouting"


class Credential(BaseModel):
    username: str
    password: str


class Device(BaseModel):
    name: str
    address: IPvAnyAddress
    port: int = 22
    platform: Platform
    credentials: Credential


class DeviceResponse(BaseModel):
    name: str
    address: IPvAnyAddress
    port: int = 22
    platform: Platform


class DevicesFile(BaseModel):
    devices: List[Device]


class IPWithPortModel(BaseModel):
    address: IPvAnyAddress
    port: conint(gt=0, lt=65535)
