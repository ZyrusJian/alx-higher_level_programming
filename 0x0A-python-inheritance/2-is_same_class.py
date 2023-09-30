#!/usr/bin/python3
"""
This module contains a function is_same_class that returns Truei
if the object is exactly an instance of the specified class;
otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check against.

    Returns:
        bool: True if the object is exactly an instance
        of the specified class; otherwise False.
    """
    return type(obj) is a_class
