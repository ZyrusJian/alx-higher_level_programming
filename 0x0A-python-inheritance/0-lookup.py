#!/usr/bin/python3
"""
This module contains a function that returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (object): The object to lookup.

    Returns:
        list: A list of strings representing the available attributes
        and methods of the object.
    """
    return dir(obj)
