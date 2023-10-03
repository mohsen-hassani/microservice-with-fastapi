import dataclasses

from fastapi import HTTPException, status

from databases import BaseDatabase, ObjectNotExistsException
from models.schemas import UserRegisterSchema, UserSchema, UserTokenSchema, UserLoginSchema
from models.domains import DBUser
from utils import encrypt, decrypt

UNAUTHORIZED_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='invalid credentials',
    headers={'WWW-Authenticate': 'bearer'}
)


class BaseService:
    def __init__(self, db: BaseDatabase):
        self.db = db


class RegisterUserService(BaseService):
    def exec(self, user: UserRegisterSchema) -> UserTokenSchema:
        db_user = DBUser(**user.model_dump(), id_=None)
        user_id = self.db.insert(db_user)
        token = UserTokenSchema(token=encrypt(str(user_id)))
        return token


class LoginUserService(BaseService):
    def exec(self, user: UserLoginSchema) -> UserTokenSchema:
        try:
            db_user: DBUser = self.db.get_by_email(user.email)
        except ObjectNotExistsException:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='invalid email/password',
            )
        if db_user.password != user.password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='invalid email/password',
            )
        token = UserTokenSchema(token=encrypt(str(db_user.id_)))
        return token


class GetCurrentUserService(BaseService):
    def exec(self, token: str) -> UserSchema:
        user_id = decrypt(token)
        try:
            db_user: DBUser = self.db.get_by_id(int(user_id))
        except ObjectNotExistsException:
            raise UNAUTHORIZED_EXCEPTION
        user_dict = dataclasses.asdict(db_user)
        del user_dict["password"]
        return UserSchema(**user_dict)


class UpdateCurrentUserService(BaseService):
    def exec(self, current_user: UserSchema, data: UserSchema) -> UserSchema:
        db_user = self.db.update_by_id(int(current_user.id_), data)
        user_dict = dataclasses.asdict(db_user)
        del user_dict["password"]
        return UserSchema(**user_dict)
