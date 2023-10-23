import bcrypt

from datetime import datetime, timedelta

from jose import jwt

from src.config import settings


def create_access_token(sub: str | int):
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"exp": expire, "sub": str(sub)}
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token


def hash_password(plain_password: str) -> bytes:
    password = bytes(plain_password, 'utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(bytes(plain_password, "utf-8"), bytes(hashed_password, 'utf-8'))