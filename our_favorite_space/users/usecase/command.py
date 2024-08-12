from abc import ABC, abstractmethod

from users.domain.user import User
from users.vo.type import EventTimeType


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
