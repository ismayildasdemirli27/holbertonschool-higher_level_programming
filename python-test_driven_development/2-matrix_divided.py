#!/usr/bin/python3
"""
This module provides a function `matrix_divided` that divides all
elements of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int or float): The divisor.

    Returns:
        list: A new matrix containing the divided elements rounded
        to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix have different sizes.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is 0.
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    err_size = "Each row of the matrix must have the same size"

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_msg)
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(err_msg)

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(err_size)

    return [[round(item / div, 2) for item in row] for row in matrix]
