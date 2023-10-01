#!/usr/bin/python3
"""
This module contains a function write_file that writes a string
to a text file (UTF8) and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.

    Raises:
        TypeError: If the filename or text is not a string.

    """
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
