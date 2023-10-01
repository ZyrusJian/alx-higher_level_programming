#!/usr/bin/python3
"""
This module contains a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    A class that represents an integer with inverted == and != operators.
    """
    def __eq__(self, other):
        """
        Inverts the == operator.

        Args:
            other (int): The other integer to compare to.

        Returns:
            True if the integers are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.

        Args:
            other (int): The other integer to compare to.

        Returns:
            True if the integers are equal, False otherwise.
        """
        return super().__eq__(other)
