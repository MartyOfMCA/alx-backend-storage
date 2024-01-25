#!/usr/bin/env python3
"""
Define a class used as Cache.
"""
import redis
from uuid import uuid4
from typing import (
        Union,
        Callable
        )
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Counts the number of calls to the given
    callback.

    Parameters:
        callback : Callable
        The callback method to track.

    Returns:
        A wrapper instance tracking calls
        to given callback.
    """
    @wraps(method)
    def wrapper(self, data) -> str:
        """
        Tracks the number of calls to the
        decorated method.

        Paraeters:
            data : Union
            The value passed to decorated
            method.

        Returns:
            The number of time the callback
            is fired.
        """
        self._redis.incr(method.__qualname__)
        return (method(self, data))
    return (wrapper)


class Cache:
    """
    Store an instance of a Redis client.
    """

    def __init__(self):
        """ Setup new instance. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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

    def get(self, key: str, fn: Callable = None):
        """
        Retrieve the value for the given key.

        Parameters:
            key : string
            The key whose value is to be
            retrieved.

            fn : Callable, optional
            An optional callback method
            to convert the data retrieved
            to an appropriate type.

        Returns:
            The value for the given key
            otherwise None.
        """
        if (fn is int):
            return (self.get_int(self._redis.get(key)))
        if (fn is str):
            return (self.get_str(self._redis.get(key)))
        if (fn is None):
            return (self._redis.get(key))
        else:
            return (fn(self._redis.get(key)))

    def get_str(self, data):
        """
        Converts the given data to a string
        in the UTF-8 encoding format.

        Parameters:
            data : byte
            The data retrieved as a byte.

        Return:
            A string representation
            of data.
        """
        return (data.decode("utf-8"))

    def get_int(self, data):
        """
        Converts the given data to an int.
                                                   Parameters:
            data : byte
            The data retrieved as a byte.
                                                   Return:
            An int representation
            of data.
        """
        return (int(data.decode("utf-8")))
