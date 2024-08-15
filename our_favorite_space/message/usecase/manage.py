from abc import ABC, abstractmethod

from message.domain.message import Message


class SendUseCase(ABC):
    @abstractmethod
    def send(self) -> None:
        pass


class GetInfoUseCase(ABC):
    @abstractmethod
    def get_info(self, id: int) -> Message:
        pass
