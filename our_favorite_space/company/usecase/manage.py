from abc import ABC, abstractmethod

from our_favorite_space.company.domain.company import Company


class CreateUseCase(ABC):
    @abstractmethod
    def create(self) -> Company:
        pass


class GetInfoUseCase(ABC):
    @abstractmethod
    def get_info(self, name: str) -> Company:
        pass


class ModifyUseCase(ABC):
    @abstractmethod
    def modify(self, name: str) -> Company:
        pass


class DeleteUseCase(ABC):
    @abstractmethod
    def delete(self, name: str) -> None:
        pass
