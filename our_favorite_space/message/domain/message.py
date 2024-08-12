from dataclasses import dataclass

from message.vo.type import MessageType
from users.domain.user import User


@dataclass
class Message:
    id: int
    type: MessageType
    content: str
    send: User
    to: User
