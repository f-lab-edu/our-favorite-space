from abc import ABC, abstractmethod

from our_favorite_space.users.domain.type import EventTime


class SetEventTimeCase(ABC):
    @abstractmethod
    def set_event_time(self, event_time: EventTime) -> None:
        pass
