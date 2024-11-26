from contextlib import asynccontextmanager

from app.caching.mixins.cache import RedisCacheMixin
from app.database.mixins.session import SessionManagementMixin


class BaseService(RedisCacheMixin, SessionManagementMixin):
    __repository_class__ = None

    @asynccontextmanager
    async def get_repo(self, *repo):
        async with self.get_session() as session:
            # If there are no repo classes provided, create instance
            # of __repository_class__
            if len(repo) == 0:
                if self.__repository_class__ is None:
                    raise RuntimeError("No repository class or classes provided")
                yield self.__repository_class__(session)
            # If there is only one repo class provided then
            # yield single instance
            elif len(repo) == 1:
                yield repo[0](session)
            # Else create and return instances for all classes
            else:
                yield [repo(session) for repo in repo]
