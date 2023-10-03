from fastapi import Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

from databases import InMemoryDictDatabase, BaseDatabase
from models.schemas import UserSchema
from services import GetCurrentUserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db() -> BaseDatabase:
    return InMemoryDictDatabase()


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db=Depends(get_db)) -> UserSchema:
    service = GetCurrentUserService(db)
    return service.exec(token)
