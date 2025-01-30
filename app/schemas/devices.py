from enum import Enum
from pydantic import BaseModel, IPvAnyAddress
from typing import List


class Platform(str, Enum):
    cisco_ios = "cisco_ios"
    juniper = "juniper"


class Credential(BaseModel):
    username: str
    password: str


class Device(BaseModel):
    name: str
    address: IPvAnyAddress
    platform: Platform
    credentials: Credential


class DevicesFile(BaseModel):
    devices: List[Device]
