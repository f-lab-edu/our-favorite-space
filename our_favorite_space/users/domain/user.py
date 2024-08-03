from dataclasses import dataclass

from our_favorite_space.users.domain.type import EventTime, UserType


@dataclass
class User:
    id: int
    type: UserType
    company: str
    event_times: list[EventTime]
