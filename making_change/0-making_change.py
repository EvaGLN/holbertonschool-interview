#!/usr/bin/python3
"""Change comes from within"""

def makeChange(coins, total):
    """ewest number of coins to meet a given amount total"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if total <= 0:
            break
        coin_count += total // coin
        total = total % coin
    if total != 0:
        return -1
    return coin_count
