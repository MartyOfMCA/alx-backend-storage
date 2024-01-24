#!/usr/bin/env python3
"""
Define a class used as Cache.
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """
    Store an instance of a Redis client.
    """

    def __init__(self):
        """ Setup new instance. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis using
        a randomly generated string as the
        key.

        Parameters:
            data : string
            The value to store.

        Returns:
            The generated key as a string.
        """
        uuid = str(uuid4())
        self._redis.set(uuid, data)

        return (uuid)
