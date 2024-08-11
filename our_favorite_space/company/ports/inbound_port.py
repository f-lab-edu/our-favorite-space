from our_favorite_space.company.domain.company import Company
from our_favorite_space.company.ports.outbound_port import (
    DeleteCompanyOutboundPort,
    LoadCompanyOutboundPort,
    SaveCompanyOutboundPort,
)
from our_favorite_space.company.usecase.manage import (
    CreateUseCase,
    DeleteUseCase,
    GetInfoUseCase,
    ModifyUseCase,
)


class CompanyCreateInboundPort(CreateUseCase):
    def __init__(self, save_company_port: SaveCompanyOutboundPort):
        self.save_company_port = save_company_port

    def create(self, name: str, email_domain: str) -> Company:
        company = Company(name=name, email_domain=email_domain)
        return self.save_company_port.save(company)


class CompanyGetInfoInboundPort(GetInfoUseCase):
    def __init__(self, load_company_port: LoadCompanyOutboundPort):
        self.load_company_port = load_company_port

    def get_info(self, name: str) -> Company:
        return self.load_company_port.get(name)


class CompanyModifyInboundPort(ModifyUseCase):
    def __init__(
        self,
        load_company_port: LoadCompanyOutboundPort,
        save_company_port: SaveCompanyOutboundPort,
    ):
        self.load_company_port = load_company_port
        self.save_company_port = save_company_port

    def modify(self, name: str, **data) -> Company:
        company = self.load_company_port.get(name)

        for key, value in data.items():
            if hasattr(company, key):
                setattr(company, key, value)

        return self.save_company_port.save(company)


class CompanyDeleteInboundPort(DeleteUseCase):
    def __init__(
        self,
        load_company_port: LoadCompanyOutboundPort,
        delete_company_port: DeleteCompanyOutboundPort,
    ):
        self.load_company_port = load_company_port
        self.delete_company_port = delete_company_port

    def delete(self, name: str) -> None:
        company = self.load_company_port.get(name)
        self.delete_company_port.delete(company)
