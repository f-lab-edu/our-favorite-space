from dataclasses import dataclass
from our_favorite_space.users.domain.type import UserType


@dataclass
class User:
    id: int
    type: UserType
