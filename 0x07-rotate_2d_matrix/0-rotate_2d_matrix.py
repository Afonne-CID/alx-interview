#!/usr/bin/python3
""" Rotate 2D Matrix Module
"""


def rotate_2d_matrix(matrix):
    """ Rotate 2d matrix 90 deg.
    """
    if not len(matrix) or len(matrix) != len(matrix[0]):
        return
    n = len(matrix)
    for row in range(n // 2):
        first, last, offset = row, n - 1 - row, 0
        for i in range(first, last):
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
            offset += 1
