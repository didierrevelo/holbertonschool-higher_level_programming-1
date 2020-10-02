#!/usr/bin/python3
""" matrix divide method """


def matrix_divided(matrix, div):
    """ matrix_divide

    Args:
        matrix ([list]): [is a list of lists]
        div ([int or float])

    Raises:
        TypeError: [matrix must be a matrix (list of lists) of integers/floats]
        TypeError: [matrix must be a matrix (list of lists) of integers/floats]
        ZeroDivisionError: [division by zero]
        TypeError: [div must be a number]

    Returns:
        [matrix]: [matrix[iterartor] / div]
    """
    Err = {
        1: "matrix must be a matrix (list of lists) of integers/floats",
        2: "Each row of the matrix must have the same size"
    }
    if not isinstance(matrix, list):
        raise TypeError(Err[1])
    if len(matrix) == 0:
        raise TypeError(Err[1])
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(Err[1])
        if len(row) == 0:
            raise TypeError(Err[1])
        if len(matrix[0]) is not len(row):
            raise TypeError(Err[2])
        for num in row:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError(Err[1])
    return [[round(num / div, 2)for num in row]for row in matrix]
