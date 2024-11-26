from contextlib import asynccontextmanager


class SessionManagementMixin:
    _session_factory = None

    def __init__(self, context=None):
        self.context = context

    @asynccontextmanager
    async def get_session(self):
        async with self.__class__._session_factory() as session:
            async with session.begin():
                yield session

    @classmethod
    def set_session_factory(cls, session_factory):
        cls._session_factory = session_factory


def set_global_session_factory(session_factory):
    SessionManagementMixin.set_session_factory(session_factory)
