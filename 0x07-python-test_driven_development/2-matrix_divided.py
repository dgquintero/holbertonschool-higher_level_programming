#!/usr/bin/python3
def matrix_divided(matrix, div):

    size_= len(matrix[0])
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

    return [[round(j / div, 2) for j in i] for i in matrix]
