#!/usr/bin/env python3
"""
Define a function to implement an expiring
web cache.
"""
from typing import Callable
import requests
import redis
from functools import wraps


_redis = redis.Redis()


def track_url(method: Callable) -> Callable:
    """
    Track the number of times callback function
    accesses URL.

    Parameters:
        method : Callable
        The callack method to track.

    Returns:
        A wrapper instance to the response
        to the callback method
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Track requests made to a given
        URL.

        Parameters:
            url : string
            The URL to the resource to fetch.

        Returns:
            The response to the request made.
        """
        key = "cache"
        value = _redis.get(key)
        if (value):
            return (value.decode("utf-8"))

        response = method(url)
        _redis.incr(f"count:{url}")
        _redis.set(key, response)
        _redis.expire(key, 10)
        return (response)
    return (wrapper)


@track_url
def get_page(url: str) -> str:
    """
    Requests for the given URL.

    Parameters:
        url : string
        The URL to fetch.

    Returns:
        The HTML contents from the
        given URL.
    """
    print(int(_redis.get(f"count:{url}").decode("utf-8")))
    with requests.get(url) as response:
        return (response.text)
