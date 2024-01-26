#!/usr/bin/env python3
"""
Defines a function to obtain HTML
content for a given url.
"""
from requests import get


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
