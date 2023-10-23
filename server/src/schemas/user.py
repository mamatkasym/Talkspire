import re

from pydantic import BaseModel, EmailStr, Field, field_validator

STRONG_PASSWORD_PATTERN = re.compile(r"^(?=.*\d)(?=.*[!@#$%^&*])[\w!@#$%^&*]{6,128}$")


class User(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)

    @field_validator("password", mode="after")
    def valid_password(cls, password: str) -> str:
        if not re.match(STRONG_PASSWORD_PATTERN, password):
            raise ValueError(
                "Password must contain at least "
                "one lower character, "
                "one upper character, "
                "digit or "
                "special symbol"
            )

        return password

    is_active: bool | None = True
    is_superuser: bool | None = False
    full_name: str | None = None
