from dataclasses import dataclass

from our_favorite_space.message.vo.type import MessageType


@dataclass
class Message:
    id: int
    type: MessageType
    content: str
