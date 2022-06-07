#!/usr/bin/python3
'''Making Change Module
'''


def makeChange(coins, total):
    '''Determines the fewest number of coins needed to meet
        a given amount total.
    '''
    if total <= 0:
        return 0
    tmp = [0] + [float("inf")] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            tmp[i] = min(tmp[i], tmp[i - coin] + 1)
    return tmp[-1] if tmp[-1] != float("inf") else -1
