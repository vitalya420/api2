# cache.py

from abc import ABC
from warnings import warn


class RedisCacheMixin(ABC):
    _redis = None

    @classmethod
    def set_redis(cls, instance):
        cls._redis = instance

    @classmethod
    def clear_redis(cls):
        cls._redis = None

    @classmethod
    async def cache_get(cls, key):
        if cls._redis is None:
            warn(
                f"Attempted to fetch key '{key}' from cache in {cls.__name__}, "
                "but Redis is not initialized. Returning None to fall back on database requests.",
                UserWarning,
            )
            return None
        key = key.encode("utf-8") if isinstance(key, str) else key
        # i will implement

    @classmethod
    async def cache_set(cls, key, value, *redis_set_args, **redis_set_kwargs):
        pass

    @classmethod
    async def cache_delete(cls, key):
        pass

    @classmethod
    async def cache_object(cls, object_, *redis_set_args, **redis_set_kwargs):
        pass
