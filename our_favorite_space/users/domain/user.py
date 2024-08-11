from dataclasses import dataclass, field

from our_favorite_space.company.domain.company import Company
from our_favorite_space.users.vo.type import EventTime, UserType


@dataclass
class User:
    id: int
    name: str
    type: UserType
    company: Company
    event_times: list[EventTime] = field(default_factory=list)
