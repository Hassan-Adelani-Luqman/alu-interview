#!/usr/bin/python3
"""
Module that contains min_operations function.
"""


def min_operations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n 'H' characters in the file.

    Args:
        n (int): Target number of H characters.

    Returns:
        int: Minimum number of operations needed.
             Returns 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    if n > 1:
        operations += n

    return operations