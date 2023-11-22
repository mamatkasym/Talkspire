from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from src.api.v1.auth.backends import auth_backend
from src.api.v1.auth.manager import get_user_manager
from src.models.user import User
from src.schemas.user import UserRead, UserCreate

router = APIRouter()

fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="",
    tags=["auth"],
)