from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class User:
    """Модель для создания пользователя (все поля обязательны)."""
    firstName: str
    lastName: str
    email: str
    password: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class UserUpdate:
    """Модель для обновления (все поля опциональны)."""
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

    def to_dict(self) -> dict:
        return {k: v for k, v in asdict(self).items() if v is not None}