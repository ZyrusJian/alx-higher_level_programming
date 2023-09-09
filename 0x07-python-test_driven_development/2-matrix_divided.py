#!/usr/bin/python3
"""Divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix (list): A list of lists of ints/floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists, or
        each row is not the same size, or div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix where each element is divided by div.
        Rounded to 2 decimal places.
    """

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(\
                'matrix must be a matrix(list of lists) of integers/floats')

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError('matrix must be a\
                            matrix(list of lists) of integers/floats')
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError('matrix must be a\
                                matrix(list of lists) of integers/floats')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(item / div, 2) for item in row] for row in matrix]
