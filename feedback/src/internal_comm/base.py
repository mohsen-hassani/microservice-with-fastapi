import dataclasses
from abc import ABC, abstractmethod
from enum import Enum, auto

from src.models.domains import UserID


class Statuses(Enum):
    OK = auto()
    FAILED = auto()


@dataclasses.dataclass
class InternalResponse:
    status: Statuses
    status_code: int | None = None
    body: dict | None = None
    exception: Exception | None = None


class BaseInternalCommunication(ABC):
    @abstractmethod
    def authenticate_user(self, user_token: str) -> UserID | None:
        raise NotImplementedError()
