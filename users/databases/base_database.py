from abc import ABC, abstractmethod
from models.domains import DBUser
from models.schemas import UserSchema


class BaseDatabase(ABC):
    @abstractmethod
    def insert(self, data: DBUser) -> int:
        raise NotImplementedError()

    @abstractmethod
    def get_by_id(self, id_: int) -> DBUser:
        raise NotImplementedError()

    @abstractmethod
    def update_by_id(self, id_: int, data: UserSchema) -> DBUser:
        raise NotImplementedError()

    @abstractmethod
    def get_by_email(self, email: str) -> DBUser:
        raise NotImplementedError()
