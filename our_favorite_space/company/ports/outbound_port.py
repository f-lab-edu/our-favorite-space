from abc import ABC

from company.domain.company import Company


class LoadCompanyOutboundPort(ABC):
    def get(self, id: int) -> Company:
        pass


class SaveCompanyOutboundPort(ABC):
    def save(self, company: Company) -> Company:
        pass


class DeleteCompanyOutboundPort(ABC):
    def delete(self, company: Company) -> None:
        pass
