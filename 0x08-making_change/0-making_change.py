#!/usr/bin/python3
"""
    Determine the fewest number of coins needed to meet a given total.

Args:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount of money you want to make change for.

Returns:
    int: The fewest number of coins needed to make the change,
    or -1 if it is not possible.
    """


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total >= coin:
            num = total // coin
            count += num
            total -= coin * num

        if total == 0:
            return count

    return -1
