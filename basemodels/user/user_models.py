from dataclasses import dataclass, asdict
from typing import Optional

# Data model
@dataclass
class User:
    firstName: str
    lastName: str
    email: str
    password: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class UserUpdate:
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

    def to_dict(self) -> dict:
        return {k: v for k, v in asdict(self).items() if v is not None}