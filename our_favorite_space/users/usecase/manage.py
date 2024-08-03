from abc import ABC, abstractmethod


class CreateUseCase(ABC):
    @abstractmethod
    def create(self) -> None:
        pass


class GetInfoUseCase(ABC):
    @abstractmethod
    def get_info(self, id: int) -> None:
        pass


class ModifyUseCase(ABC):
    @abstractmethod
    def modify(self, id: int) -> None:
        pass
