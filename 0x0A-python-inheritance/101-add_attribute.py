#!/usr/bin/python3
"""
This module contains a function add_attribute that adds a new attribute
to an object if it's possible.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj (object): The object to add the attribute to.
        name (str): The name of the attribute.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
