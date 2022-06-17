#!/usr/bin/python3
"""Prime game module
Interview Question.
"""


def isWinner(x, nums):
    """With `x` rounds, returns the winner of a prime game.
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    filter = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not filter[i]:
            continue
        for j in range(i * i, n + 1, i):
            filter[j] = False
    filter[0] = filter[1] = False
    c = 0
    for i in range(len(filter)):
        if filter[i]:
            c += 1
        filter[i] = c
    pl1 = 0
    for n in nums:
        pl1 += filter[n] % 2 == 1
    if pl1 * 2 == len(nums):
        return None
    if pl1 * 2 > len(nums):
        return "Maria"
    return "Ben"
