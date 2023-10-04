from pydantic import BaseModel
from pydantic import EmailStr

from models.domains import UserID


class UserRegisterSchema(BaseModel):
    email: EmailStr
    password: str
    first_name: str = ""
    last_name: str = ""


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserSchema(BaseModel):
    id_: UserID
    email: EmailStr
    first_name: str
    last_name: str


class UserTokenSchema(BaseModel):
    token: str
