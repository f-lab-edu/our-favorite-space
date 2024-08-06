from abc import ABC, abstractmethod


class SendUseCase(ABC):
    @abstractmethod
    def send(self) -> None:
        pass


class GetInfoUseCase(ABC):
    @abstractmethod
    def get_info(self, id: int) -> None:
        pass
