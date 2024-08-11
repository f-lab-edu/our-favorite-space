from abc import ABC, abstractmethod

from our_favorite_space.space.domain.space import Space


class CreateUseCase(ABC):
    @abstractmethod
    def create(self) -> Space:
        pass


class GetInfoUseCase(ABC):
    @abstractmethod
    def get_info(self, id: int) -> Space:
        pass


class ModifyUseCase(ABC):
    @abstractmethod
    def modify(self, id: int) -> Space:
        pass


class DeleteUseCase(ABC):
    @abstractmethod
    def delete(self, id: int) -> None:
        pass
