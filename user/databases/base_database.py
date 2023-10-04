from abc import ABC, abstractmethod
from models.domains import DBUser, UserID
from models.schemas import UserSchema


class BaseDatabase(ABC):
    @abstractmethod
    def insert(self, data: DBUser) -> UserID:
        raise NotImplementedError()

    @abstractmethod
    def get_by_id(self, id_: UserID) -> DBUser:
        raise NotImplementedError()

    @abstractmethod
    def update_by_id(self, id_: UserID, data: UserSchema) -> DBUser:
        raise NotImplementedError()

    @abstractmethod
    def get_by_email(self, email: str) -> DBUser:
        raise NotImplementedError()
