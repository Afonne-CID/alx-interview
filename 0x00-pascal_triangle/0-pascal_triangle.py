#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """ Returns a list of lists of integers representing the
        Pascal's triangle of `n`
    """
    my_list = []
    if (n > 0):
        for i in range(1, n + 1):
            inner = []
            cnt = 1
            for j in range(1, i + 1):
                inner.append(cnt)
                cnt = cnt * (i - j) // j
            my_list.append(inner)
    return my_list
