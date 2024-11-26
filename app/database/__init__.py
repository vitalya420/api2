from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from app.database.mixins.session import set_global_session_factory

engine = create_async_engine("sqlite+aiosqlite:///test.db")

async_session_factory = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()

set_global_session_factory(async_session_factory)
