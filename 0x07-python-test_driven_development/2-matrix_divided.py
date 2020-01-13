#!/usr/bin/python3
"""Module to div a matrix for a number"""


def matrix_divided(matrix, div):
    """Function that returns the division of all elements of a  matrix for
    an integer."""
    new_matrix = []
    size_ = len(matrix[0])
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div is 0:
        raise ZeroDivisionError("division by zero")

    if type(div) == float:
        div = int(div)

    for i in matrix:
        if len(i) != size_:
            raise TypeError("Each row of the matrix must have the same size")

        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
of integers/floats")
    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]
    return (new_matrix)
