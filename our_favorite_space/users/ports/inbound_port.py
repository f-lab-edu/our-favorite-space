from company.ports.outbound_port import LoadCompanyOutboundPort
from users.domain.user import User
from users.ports.outbound_port import LoadUserOutboundPort, SaveUserOutboundPort
from users.usecase.command import SetEventTimeUseCase
from users.usecase.manage import (
    CreateUseCase,
    DeleteUseCase,
    GetInfoUseCase,
    ModifyUseCase,
)
from users.vo.type import EventTime, EventTimeType, UserType


class UserCreateInboundPort(CreateUseCase):
    def __init__(
        self,
        save_user_port: SaveUserOutboundPort,
        load_company_port: LoadCompanyOutboundPort,
    ):
        self.load_company_port = load_company_port
        self.save_user_port = save_user_port

    def create(self, name: str, company_id: int) -> User:
        company = self.load_company_port(company_id)
        user = User(name=name, type=UserType.NORMAL, company=company)
        return self.save_user_port.save(user)

    def create_admin(self, name: str, company_id: int) -> User:
        company = self.load_company_port(company_id)
        user = User(name=name, type=UserType.COMPANY_ADMIN, company=company)
        return self.save_user_port.save(user)


class UserGetInfoInboundPort(GetInfoUseCase):
    def __init__(self, load_user_port: LoadUserOutboundPort):
        self.load_user_port = load_user_port

    def get_info(self, id: int) -> User:
        return self.load_user_port.get(id)


class UserModifyInboundPort(ModifyUseCase):
    def __init__(
        self,
        load_user_port: LoadUserOutboundPort,
        save_user_port: SaveUserOutboundPort,
    ):
        self.load_user_port = load_user_port
        self.save_user_port = save_user_port

    def modify(self, id: int, **data) -> User:
        user = self.load_user_port.get(id)

        for key, value in data.items():
            if hasattr(user, key):
                setattr(user, key, value)

        return self.save_user_port.save(user)


class UserDeleteInboundPort(DeleteUseCase):
    def __init__(self, load_user_port: LoadUserOutboundPort):
        self.load_user_port = load_user_port

    def delete(self, id: int) -> None:
        user = self.load_user_port.get(id)
        self.load_user_port.delete(user)


class UserEventTimeSetInboundPort(SetEventTimeUseCase):
    def __init__(
        self, load_user_port: LoadUserOutboundPort, save_user_port: SaveUserOutboundPort
    ):
        self.load_user_port = load_user_port
        self.save_user_port = save_user_port

    def set(
        self,
        user: User,
        event_time_type: EventTimeType,
        hour: int,
        min: int,
        weekday: set[int],
    ) -> User:
        user = self.load_user_port.get(user.id)
        user.event_times[event_time_type] = EventTime(
            hour=hour, min=min, weekday=weekday
        )
        return self.save_user_port.save(user)
