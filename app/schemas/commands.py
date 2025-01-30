from pydantic import BaseModel
from .devices import Platform
from typing import Dict


class CommandSet(BaseModel):
    ping: str
    traceroute: str
    bgp_route: str


class CommandsFile(BaseModel):
    commands: Dict[Platform, CommandSet]
