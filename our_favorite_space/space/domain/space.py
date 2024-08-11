from dataclasses import dataclass

from our_favorite_space.space.vo.type import SpaceType


@dataclass
class Space:
    name: str
    description: str
    type: SpaceType
