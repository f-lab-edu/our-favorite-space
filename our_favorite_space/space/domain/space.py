from dataclasses import dataclass

from space.vo.type import SpaceType


@dataclass
class Space:
    name: str
    description: str
    type: SpaceType
    id: int = None
