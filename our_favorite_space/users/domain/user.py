from dataclasses import dataclass

from our_favorite_space.users.vo.type import EventTime, UserType


@dataclass
class User:
    id: int
    name: str
    type: UserType
    company: str
    event_times: list[EventTime]
