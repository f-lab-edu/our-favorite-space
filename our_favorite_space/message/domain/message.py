from dataclasses import dataclass

from message.vo.type import MessageType
from users.domain.user import User


@dataclass
class Message:
    type: MessageType
    content: str
    send: User
    to: User
    id: int = None
