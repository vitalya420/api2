from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Optional, Dict, Any

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

class SessionManagementMixin:
    _session_factory: Optional[async_sessionmaker]

    def __init__(self, context: Optional[Dict[Any, Any]] = None):
        pass

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession]:
        pass

    @classmethod
    def set_session_factory(cls, session_factory: async_sessionmaker):
        pass

def set_global_session_factory(session_factory: async_sessionmaker) -> None:
    pass
