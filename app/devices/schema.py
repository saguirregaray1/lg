from enum import Enum
from pydantic import BaseModel, IPvAnyAddress, field_validator
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
    port: int = 22
    platform: Platform
    credentials: Credential


class DevicesFile(BaseModel):
    devices: List[Device]


class IPv4WithPortModel(BaseModel):
    address: str

    @field_validator("address", mode="after")
    @classmethod
    def validate_ipv4_with_port(cls, value: str) -> str:
        try:
            ip_str, port_str = value.rsplit(":", 1)
            ip = IPvAnyAddress(ip_str)
            port = int(port_str)

            if not (0 <= port <= 65535):
                raise ValueError("Port must be between 0 and 65535")

        except (ValueError, IndexError):
            raise ValueError(
                "Invalid format. Expected IPv4:Port (e.g., 192.168.1.1:8080)"
            )

        return value
