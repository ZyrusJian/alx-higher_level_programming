#!/usr/bin/python3
"""
This script adds all arguments to a Python list, and then saves them to a file.
"""

import sys
from os import path
from typing import List
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_item(args: List[str], filename: str) -> List[str]:
    """
    Adds all arguments to a Python list, and then saves them to a file.

    Args:
        args (List[str]): The list of arguments to add to the list.
        filename (str): The name of the file to save the list to.

    Returns:
        List[str]: The updated list of items.
    """
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(args)
    save_to_json_file(my_list, filename)
    return my_list


if __name__ == '__main__':
    args = sys.argv[1:]
    add_item(args, 'add_item.json')
