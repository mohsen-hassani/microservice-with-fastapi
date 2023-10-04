from fastapi import Header, Depends
from typing import Annotated
from cryptography.fernet import InvalidToken

from src.databases import InMemoryDictDatabase, BaseDatabase
from src.internal_comm import BaseInternalCommunication, RestInternalCommunication
from src.models.domains import UserID


def get_db() -> BaseDatabase:
    return InMemoryDictDatabase()


def parse_token(authorization: Annotated[str | None, Header()] = None) -> str | None:
    if not authorization:
        return None
    try:
        token = authorization.split()
        return token[1]
    except (IndexError, InvalidToken):
        return None


def get_inter_comm():
    return RestInternalCommunication()


def get_user_id(
    token: str | None = Depends(parse_token), inter_comm: BaseInternalCommunication = Depends(get_inter_comm)
) -> UserID | None:
    if not token:
        return None
    return inter_comm.authenticate_user(token)
