from abc import ABC, abstractmethod

from our_favorite_space.users.domain.user import User


class CreateUseCase(ABC):
    @abstractmethod
    def create(self) -> User:
        pass

    @abstractmethod
    def create_admin(self) -> User:
        pass


class GetInfoUseCase(ABC):
    @abstractmethod
    def get_info(self, id: int) -> User:
        pass


class ModifyUseCase(ABC):
    @abstractmethod
    def modify(self, id: int) -> User:
        pass


class DeleteUseCase(ABC):
    @abstractmethod
    def delete(self, id: int) -> None:
        pass
