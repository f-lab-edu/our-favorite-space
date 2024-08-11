from abc import ABC, abstractmethod

from our_favorite_space.rating.domain.rating import Rating


class CreateUseCase(ABC):
    @abstractmethod
    def create(self) -> Rating:
        pass


class GetInfoUseCase(ABC):
    @abstractmethod
    def get_info(self, id: int) -> Rating:
        pass


class DeleteUseCase(ABC):
    @abstractmethod
    def delete(self, id: int) -> None:
        pass
