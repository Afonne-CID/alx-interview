#!/usr/bin/python3
'''Minimum Operations (Interview Question) module
'''


def minOperations(n: int) -> int:
    '''Calculates the fewest number of operations needed to result
        in exactly `n` `H` characters in a file that has only a singe `H` 
        character
    '''
    if (not n or n <= 1):
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(int(n / i)) + i
