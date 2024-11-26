from sqlalchemy import Column, Integer

from app.caching.mixins.cachable import CachableMixin
from app.database import Base


class BaseModelWithID(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class BaseCachableModelWithID(BaseModelWithID, CachableMixin):
    __abstract__ = True

    def get_key(self):
        return f"{self.__tablename__}:{self.id}"
