#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """ Returns a list of lists of integers representing the
        Pascal's triangle of `n`

        Args:
            n (int): An integer to be represented in the pascal's triangle
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
        tmp_list = my_list[-1]
        to_append = []

        while (tmp_length > 0):
            if (tmp_list[(length - tmp_length) + 1]):
                to_append.append(tmp_list[length - tmp_length]
                                 + tmp_list[(length - tmp_length) + 1])
            tmp_length -= 1
        print("The value of to_append = {}".format(to_append))
        to_append.append(1)
        to_append.insert(0, 1)
        my_list.append(to_append)

        n -= 1

    return my_list
