#!/usr/bin/python3
"""
2-matrix_divided module
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    Returns a new matrix with elements rounded to 2 decimal places.
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_msg)
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(err_msg)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
