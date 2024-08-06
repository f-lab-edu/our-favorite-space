from dataclasses import dataclass
from enum import Enum


class UserType(Enum):
    SUPER_ADMIN = 1
    COMPANY_ADMIN = 2
    NORMAL = 3


class EventTimeType(Enum):
    LUNCH = "LUNCH"


@dataclass(frozen=True)
class EventTime:
    type: EventTimeType
    hour: int
    min: int
    weekday: list[int]
