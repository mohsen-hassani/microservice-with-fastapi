from fastapi import APIRouter, Body, Depends

from models.schemas import UserSchema, UserTokenSchema, UserRegisterSchema, UserLoginSchema
from services import RegisterUserService, LoginUserService, UpdateCurrentUserService
from dependencies import get_db, get_current_user

user_public_router = APIRouter()
user_internal_router = APIRouter()


@user_public_router.post("/register", response_model=UserTokenSchema)
def register_user(data: UserRegisterSchema = Body(...), db=Depends(get_db)):
    service = RegisterUserService(db=db)
    return service.exec(user=data)


@user_public_router.post("/login", response_model=UserTokenSchema)
def login_user(data: UserLoginSchema = Body(...), db=Depends(get_db)):
    service = LoginUserService(db)
    return service.exec(data)


@user_public_router.get("/me", response_model=UserSchema)
def user_profile(current_user: UserSchema = Depends(get_current_user)):
    return current_user


@user_public_router.put("/me", response_model=UserSchema)
def update_profile(data: UserSchema, current_user: UserSchema = Depends(get_current_user), db=Depends(get_db)):
    service = UpdateCurrentUserService(db)
    service.exec(current_user, data)
    return current_user


@user_internal_router.get("/id")
def user_id(current_user: UserSchema = Depends(get_current_user)):
    return {"id": current_user.id_}
