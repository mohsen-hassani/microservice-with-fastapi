from pydantic import BaseModel
from pydantic import EmailStr


class UserRegisterSchema(BaseModel):
    email: EmailStr
    password: str
    first_name: str = ""
    last_name: str = ""


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserSchema(BaseModel):
    id_: int
    email: EmailStr
    first_name: str
    last_name: str


class UserTokenSchema(BaseModel):
    token: str
