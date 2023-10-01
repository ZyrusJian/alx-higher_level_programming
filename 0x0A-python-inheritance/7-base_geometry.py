#!/usr/bin/python3
"""
This module contains a class BaseGeometry that serves as a base
for other geometry classes.
"""


class BaseGeometry:
    """
    A class that serves as a base for other geometry classes.
    """
    def area(self):
        """
        Raises an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value and raises a TypeError or ValueError exception
        if the value is not an integer or is less than or equal to 0.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
