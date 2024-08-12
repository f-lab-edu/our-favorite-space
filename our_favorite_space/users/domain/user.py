from dataclasses import dataclass, field

from company.domain.company import Company
from users.vo.type import EventTime, UserType


@dataclass
class User:
    id: int
    name: str
    type: UserType
    company: Company
    event_times: dict[str, EventTime] = field(default_factory=dict)
