from abc import ABC, abstractmethod


class CreateUseCase(ABC):
    @abstractmethod
    def create(self) -> None:
        pass


class GetInfoUseCase(ABC):
    @abstractmethod
    def get_info(self, id: int) -> None:
        pass


class DeleteUseCase(ABC):
    @abstractmethod
    def delete(self, id: int) -> None:
        pass
