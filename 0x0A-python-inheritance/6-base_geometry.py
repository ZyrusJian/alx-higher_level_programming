#!/usr/bin/python3
"""
This module contains a class BaseGeometry that serves as a base for
other geometry classes.
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
