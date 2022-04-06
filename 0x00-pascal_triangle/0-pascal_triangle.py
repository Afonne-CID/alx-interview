#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """ Returns a list of lists of integers representing the
        Pascal's triangle of `n`
    """
    if (n <= 0):
        return []
    if (n == 1):
        return [[1]]
    if (n == 2):
        return [[1], [1, 1]]

    my_list = [[1], [1, 1]]

    while ((n - 2) > 0):
        length = len(my_list[-1]) - 1
        tmp_length = length
        to_append = []

        while (tmp_length > 0):
            if (my_list[-1][(length - tmp_length) + 1]):
                to_append.append(my_list[-1][length - tmp_length]
                                 + my_list[-1][(length - tmp_length) + 1])
            tmp_length -= 1
        to_append.append(1)
        to_append.insert(0, 1)
        my_list.append(to_append)

        n -= 1

    return my_list
