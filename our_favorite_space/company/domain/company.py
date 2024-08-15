from dataclasses import dataclass


@dataclass
class Company:
    id: int
    name: str
    email_domain: str
