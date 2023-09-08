#!/usr/bin/python3
"""Adds two integers
"""


def add_integer(a, b=98):
    """Adds two integers a and b.

    Args:
        a (int|float): The first number.
        b (int|float): The second number, defaults to 98.

    Returns:
        int: The sum of a and b, casted to int.

    Raises:
        TypeError: If either a or b is not int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
