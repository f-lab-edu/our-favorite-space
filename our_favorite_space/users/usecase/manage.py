from abc import ABC, abstractmethod

from users.domain.user import User


class CreateUseCase(ABC):
    @abstractmethod
    def create(self, name: str, company_id: int) -> User:
        pass

    @abstractmethod
    def create_admin(self, name: str, company_id: int) -> User:
        pass


class GetInfoUseCase(ABC):
    @abstractmethod
    def get_info(self, id: int) -> User:
        pass


class ModifyUseCase(ABC):
    @abstractmethod
    def modify(self, id: int, **data) -> User:
        pass


class DeleteUseCase(ABC):
    @abstractmethod
    def delete(self, id: int) -> None:
        pass
