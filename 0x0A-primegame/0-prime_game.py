#!/usr/bin/python3
''' Prime Game '''


def isWinner(x, nums):
    '''return the winner or None'''
    def countPrimes(n):
        ''''''
        if n < 2:
            return False
        p = 2
        prime = [True] * (n+1)
        prime[0] = prime[1] = False
        while p * p <= n:
            if prime[p] is True:
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        return prime.count(True)

    ben, maria = 0, 0
    for i in range(x):
        count = countPrimes(nums[i])
        if count % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return 'Ben'
    elif maria > ben:
        return 'Maria'
    else:
        return None
