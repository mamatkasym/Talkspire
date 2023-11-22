from fastapi import Depends
from fastapi_users import BaseUserManager
from starlette.requests import Request

from src.api.dependencies import get_user_db
from src.config import settings
from src.models.user import User


class UserManager(BaseUserManager[User, int]):
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY

    async def on_after_register(
        self, user: User, request: Request | None = None
    ) -> None:
        print(f"User {user.id} has registered")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Request | None = None
    ) -> None:
        print(f"User {user.id} has forgot their password. Reset token {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Request | None = None
    ) -> None:
        print(f"Verification requested for user {user.id}. Verification token {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)