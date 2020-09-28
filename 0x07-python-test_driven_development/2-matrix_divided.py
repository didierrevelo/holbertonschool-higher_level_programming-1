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

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[0]) is not len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if type(num) is not int and type(num) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(num / div, 2)for num in row]for row in matrix]
