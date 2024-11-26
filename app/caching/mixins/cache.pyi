"""
cache.pyi

This module provides a mixin class for caching database responses in a service-oriented architecture.

The `RedisCacheMixin` class is designed to be inherited by service classes that interact with a database.
By using this mixin, services can implement caching mechanisms to store and retrieve responses from a
Redis cache, thereby improving performance and reducing the load on the database.
"""

from abc import ABC
from typing import Union, Optional, Protocol, List, overload

from redis.asyncio import Redis

class HasBytesMagicMethod(Protocol):
    """
    Protocol for objects that implement a `__bytes__` method.
    This allows custom objects to be converted to bytes when used with Redis cache.
    """

    def __bytes__(self) -> bytes: ...

class HasGetKeyMethod(Protocol):
    """
    Protocol for objects that implement a `get_key` method.
    """

    def get_key(self) -> str: ...

class CachableObject(Protocol):
    """
    Represents an object that can be cached in Redis.
    Such objects must implement:
    - `__bytes__` for serialization
    - `get_key` for unique cache key generation
    """

    def get_key(self) -> str: ...
    def __bytes__(self) -> bytes: ...

class CachableObjectWithReferenceKeys(Protocol):
    """
    Represents an object that can be cached in Redis.
    Such objects must implement:
    - `__bytes__` for serialization
    - `get_key` for unique cache key generation
    - `get_reference_keys` for reference to unique cache key
    """

    def get_key(self) -> str: ...
    def get_reference_keys(self) -> List[str]: ...
    def __bytes__(self) -> bytes: ...

class RedisCacheMixin(ABC):
    """
    Mixin for managing Redis caching operations.

    This class provides a mechanism to integrate Redis caching into
    services, allowing database requests to be cached for improved
    performance. If Redis is not initialized, operations will log a
    warning and gracefully degrade to database calls.
    """

    _redis: Optional[Redis]

    @classmethod
    def set_redis(cls, instance: Redis):
        """
        Set the Redis instance for the class.
        """

    @classmethod
    def clear_redis(cls):
        """
        Remove the Redis instance for the class.
        """

    @classmethod
    async def cache_get(cls, key: Union[str, bytes]) -> Optional[bytes]:
        """
        Get a value from the Redis cache.
        """

    @classmethod
    async def cache_set(
        cls,
        key: Union[str, bytes],
        value: Union[bytes, HasBytesMagicMethod],
        *redis_set_args,
        **redis_set_kwargs
    ) -> None:
        """
        Set a value in the Redis cache.
        """

    @classmethod
    async def cache_delete(cls, key: Union[str, bytes]) -> None:
        """
        Delete a value from Redis cache
        """

    @classmethod
    @overload
    async def cache_object(
        cls, object_: CachableObject, *redis_set_args, **redis_set_kwargs
    ) -> None:
        """
        Cache python's object
        """

    @classmethod
    @overload
    async def cache_object(
        cls,
        object_: CachableObjectWithReferenceKeys,
        *redis_set_args,
        **redis_set_kwargs
    ) -> None:
        """
        Cache python's object with reference keys
        """

    @classmethod
    async def delete_object(cls, object_: CachableObject) -> None:
        pass
