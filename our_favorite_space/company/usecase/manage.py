from abc import ABC, abstractmethod

from company.domain.company import Company


class CreateUseCase(ABC):
    @abstractmethod
    def create(self, name: str, email_domain: str) -> Company:
        pass


class GetInfoUseCase(ABC):
    @abstractmethod
    def get_info(self, id: int) -> Company:
        pass


class ModifyUseCase(ABC):
    @abstractmethod
    def modify(self, id: int, **data) -> Company:
        pass


class DeleteUseCase(ABC):
    @abstractmethod
    def delete(self, id: int) -> None:
        pass
