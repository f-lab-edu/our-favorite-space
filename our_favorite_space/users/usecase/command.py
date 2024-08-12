from abc import ABC, abstractmethod

from our_favorite_space.users.domain.user import User
from our_favorite_space.users.vo.type import EventTime, EventTimeType


class SetEventTimeUseCase(ABC):
    @abstractmethod
    def set_event_time(
        self,
        user: User,
        event_time_type: EventTimeType,
        hour: int,
        min: int,
        weekday: set[int],
    ) -> bool:
        pass
