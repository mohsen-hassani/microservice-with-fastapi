import uuid
from models.domains import DBUser
from models.schemas import UserSchema
from .base_database import BaseDatabase
from .exceptions import ObjectNotExistsException

USER_ID = 265452349517802502818104800389817424405
USERS = {
    USER_ID: DBUser(id_=USER_ID, email="e@mail.com", password="123", first_name="Mohsen", last_name="Hassani")
}


class InMemoryDictDatabase(BaseDatabase):
    def __init__(self):
        self.__db: dict[int, DBUser] = USERS

    def insert(self, user: DBUser) -> int:
        id_ = user.id_
        if id_ is None:
            id_ = self.get_new_id()
            user.id_ = id_
        self.__db[id_] = user
        return id_

    def get_by_id(self, id_: int) -> DBUser:
        try:
            return self.__db[id_]
        except KeyError:
            raise ObjectNotExistsException()

    def update_by_id(self, id_: int, data: UserSchema) -> DBUser:
        try:
            user = self.__db[id_]
        except KeyError:
            raise ObjectNotExistsException()
        user.email = data.email
        user.first_name = data.first_name
        user.last_name = data.last_name
        return user

    def get_by_email(self, email: str) -> DBUser:
        for u in self.__db.values():
            if u.email == email:
                return u
        raise ObjectNotExistsException()

    def get_new_id(self) -> int:
        id_ = uuid.uuid4().int
        while id_ in self.__db:
            id_ = uuid.uuid4().int
        return id_
