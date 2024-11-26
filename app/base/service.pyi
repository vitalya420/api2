# service.pyi
from contextlib import asynccontextmanager
from typing import Union, Type, TypeVar, AsyncGenerator, List

from app.caching.mixins.cache import RedisCacheMixin
from .repository import BaseRepository
from app.database.mixins.session import SessionManagementMixin

RepoType = TypeVar("RepoType", bound=Type[BaseRepository])

class BaseService(RedisCacheMixin, SessionManagementMixin):
    __repository_class__: Union[RepoType, None]

    @asynccontextmanager
    async def get_repo(
        self, *repo: RepoType
    ) -> AsyncGenerator[Union[RepoType, List[RepoType], None]]:
        pass
