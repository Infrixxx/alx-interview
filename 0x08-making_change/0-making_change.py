#!/usr/bin/python3
'''Change comes from within'''
from typing import List


def makeChange(coins: List, total: int) -> int:
    ''''''
    if total <= 0:
        return 0

    coins = sorted(coins)[::-1]
    fewest_num = 0
    tot = 0
    i = 0

    for i in range(len(coins)):
        if coins[i] > total:
            continue

        while tot < total:
            tot += coins[i]
            fewest_num += 1

        if tot == total:
            return fewest_num
        else:
            tot -= coins[i]
            fewest_num -= 1

    return -1
