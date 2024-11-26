import pickle
from abc import abstractmethod


class CachableMixin(object):
    @abstractmethod
    def get_key(self):
        pass

    @classmethod
    def from_bytes(cls, data):
        return pickle.loads(data)

    def to_bytes(self):
        return pickle.dumps(self)

    def __bytes__(self):
        return self.to_bytes()
