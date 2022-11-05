#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """ Returns a list of lists of integers representing the
        Pascal's triangle of `n`
    """
    # my_list = []
    # if (n > 0):
    #     for i in range(1, n + 1):
    #         row = []
    #         cnt = 1
    #         for j in range(1, i + 1):
    #             row.append(cnt)
    #             cnt = cnt * ((i - j) // j)
    #         my_list.append(row)
    # return my_list

    if n <= 0:
        return []
    res = [[1]]
    for _ in range(n - 1):
        tmp = [0] + res[-1] + [0]
        row = []
        for i in range(len(tmp) - 1):
            row.append(tmp[i] + tmp[i+1])
        res.append(row)
    return res