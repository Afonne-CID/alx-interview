#!/usr/bin/python3
"""Prime interview question.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    players = ('Maria', 'Ben')
    winners = []
    nums_cnt = len(nums) if nums else 0
    if x <= 0:
        return None
    for i in range(x):
        n = nums[i % nums_cnt] if nums else 0
        n_nums = list(range(1, n + 1, 1))
        prime = 2
        turns = 0
        while True:
            was_removed = False
            p_multiples = list(range(prime, n + 1, prime))
            for p_multiple in p_multiples:
                if p_multiple in n_nums:
                    n_nums.remove(p_multiple)
                    was_removed = True
            turns += 1
            if was_removed:
                for val in n_nums:
                    if val > prime:
                        prime = val
                        break
            else:
                break
        winners.append(players[turns % 2])
    marias_wins = winners.count(players[0])
    bens_wins = winners.count(players[1])
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
