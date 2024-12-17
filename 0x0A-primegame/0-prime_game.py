#!/usr/bin/python3
""""Determines the winner of a prime game session."""


def isWinner(x, nums):
    """
    Determines the winner of a prime game session.

    Args:
        x (int): The number of rounds.
        nums (list of int): List of integers representing the upper limit of
        numbers for each round.

    Returns:
        str: "Maria" if Maria wins more rounds, "Ben" if Ben wins more rounds,
        or None if there is a tie or invalid input.
    """
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i*i, max_num + 1, i):
                primes[j] = False

    def count_primes(n):
        return sum(primes[:n+1])

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if count_primes(n) % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
