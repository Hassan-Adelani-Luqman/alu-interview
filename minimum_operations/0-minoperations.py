#!/usr/bin/python3
"""
Module that contains min_operations function.

Given a number n, this function calculates the fewest number
of operations needed to achieve exactly n 'H' characters.

Prototype: def min_operations(n)
Returns an integer.
If n is impossible to achieve, returns 0.
"""


def min_operations(n):
    """
    Calculates the fewest number of operations to get n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed.
             Returns 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    i = 2
    while i * i <= n:
        if n % i == 0:
            return i + min_operations(n // i)
        i += 1

    return n