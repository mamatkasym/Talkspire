from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import sessionmaker

from src.config import settings


@as_declarative()
class Base:
    pass


engine = create_async_engine(str(settings.ASYNC_DATABASE_URL))
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
