#!/usr/bin/env python3
"""
Defines a function to obtain HTML
content for a given url.
"""
from requests import get
import redis
from functools import wraps
from typing import Callable


def track(callback: Callable) -> Callable:
    """
    Tracks the number of times a particular
    URL is accessed.

    Parameters:
        callback : Callable
        The callback function to invoke.

    Returns:
        A wrapper method that tracks the
        count of requests alogside the
        normal operation of `callback`.
    """
    @wraps(callback)
    def wrapper(url):
        """
        Retrieves the HTML content of the given
        URL. Tracks the number of times a
        particular URL is accessed.

        Parameters:
            url : string
            The URL requested.

        Returns:
            The HTML page extracted from the
            given URL.
        """
        client = redis.Redis()
        client.incr(f"count:{url}")
        cache = client.get(url)

        if (cache):
            response = cache.decode("utf-8")
        else:
            response = callback(url)
            client.set(url, response, ex=10)

        return (response)
    return (wrapper)


@track
def get_page(url: str) -> str:
    """
    Retrieves the HTML content of the given
    URL.

    Parameters:
        url : string
        A valid URL to a webpage.

    Returns:
        The HTML extracted from the URL.
    """
    with get(url) as response:
        return (response.text)
