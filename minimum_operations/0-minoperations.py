#!/usr/bin/python3

"""
Given a number n, write a method that calculates the fewest # of operations.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def min_Operations(n):
    if n <= 1:
        return 0

    i = 2
    while i * i <= n:
        if n % i == 0:
            return i + min_Operations(n // i)
        i += 1

    return n