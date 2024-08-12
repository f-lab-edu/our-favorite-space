from abc import ABC

from our_favorite_space.users.domain.user import User


class LoadUserOutboundPort(ABC):
    def get(self, id: int) -> User:
        pass


class SaveUserOutboundPort(ABC):
    def save(self, user: User) -> User:
        pass


class DeleteUserOutboundPort(ABC):
    def delete(self, user: User) -> None:
        pass
