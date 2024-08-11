from dataclasses import dataclass

from our_favorite_space.message.vo.type import MessageType
from our_favorite_space.users.domain.user import User


@dataclass
class Message:
    id: int
    type: MessageType
    content: str
    send: User
    to: User
