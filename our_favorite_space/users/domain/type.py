from enum import Enum


class UserType(Enum):
    SUPER_ADMIN = 1
    COMPANY_ADMIN = 2
    NORMAL = 3
