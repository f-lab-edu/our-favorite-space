from dataclasses import dataclass


@dataclass
class Company:
    name: str
    email_domain: str
    id: int = None
