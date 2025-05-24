#!/usr/bin/python3
"""
Method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to get n H characters
    
    Args:
        n: target number of H characters
        
    Returns:
        Integer: minimum number of operations
        Returns 0 if n is impossible to achieve
    """
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1
        
        # If divisor exceeds sqrt(n), and n is > 1, n is prime
        if divisor * divisor > n and n > 1:
            operations += n
            break
            
    return operations

print(minOperations(1))      # 0
print(minOperations(2))      # 2
print(minOperations(3))      # 3
print(minOperations(4))      # 4
print(minOperations(5))      # 5
print(minOperations(6))      # 5
print(minOperations(7))      # 7
print(minOperations(8))      # 6
print(minOperations(9))      # 6
print(minOperations(10))     # 7
print(minOperations(11))     # 11
print(minOperations(12))     # 8
print(minOperations(13))     # 13
print(minOperations(14))     # 8
print(minOperations(15))     # 9
print(minOperations(16))     # 9
print(minOperations(17))     # 17
print(minOperations(18))     # 10
print(minOperations(19))     # 19
print(minOperations(20))     # 11
print(minOperations(21))     # 11
print(minOperations(22))     # 13
print(minOperations(23))     # 23
print(minOperations(24))     # 10
print(minOperations(25))     # 11
print(minOperations(26))     # 13
print(minOperations(27))     # 13
print(minOperations(28))     # 14
print(minOperations(29))     # 29
print(minOperations(30))     # 14
print(minOperations(31))     # 31
print(minOperations(32))     # 11
print(minOperations(33))     # 15
print(minOperations(34))     # 17
print(minOperations(35))     # 17
print(minOperations(36))     # 12
print(minOperations(37))     # 37
print(minOperations(38))     # 19
print(minOperations(39))     # 21
print(minOperations(40))     # 14
print(minOperations(41))     # 41
print(minOperations(42))     # 20
print(minOperations(43))     # 43
print(minOperations(44))     # 22
print(minOperations(45))     # 15
print(minOperations(46))     # 23
print(minOperations(47))     # 47
print(minOperations(48))     # 16
print(minOperations(49))     # 14
print(minOperations(50))     # 17
print(minOperations(51))     # 17
print(minOperations(52))     # 18
print(minOperations(53))     # 53
print(minOperations(54))     # 19
print(minOperations(55))     # 20
print(minOperations(56))     # 14
print(minOperations(57))     # 19
print(minOperations(58))     # 29
print(minOperations(59))     # 59
print(minOperations(60))     # 15
print(minOperations(61))     # 61
print(minOperations(62))     # 31
print(minOperations(63))     # 21
print(minOperations(64))     # 12
print(minOperations(65))     # 22
print(minOperations(66))     # 23
print(minOperations(67))     # 67
print(minOperations(68))     # 34
print(minOperations(69))     # 23
print(minOperations(70))     # 22
print(minOperations(71))     # 71
print(minOperations(72))     # 12
print(minOperations(73))     # 73
print(minOperations(74))     # 37
print(minOperations(75))     # 18
print(minOperations(76))     # 19
print(minOperations(77))     # 21
print(minOperations(78))     # 20
print(minOperations(79))     # 79
print(minOperations(80))     # 14
print(minOperations(81))     # 14
print(minOperations(82))     # 41
print(minOperations(83))     # 83
print(minOperations(84))     # 22
print(minOperations(85))     # 23
print(minOperations(86))     # 43
print(minOperations(87))     # 29
print(minOperations(88))     # 20
print(minOperations(89))     # 89
print(minOperations(90))     # 21
print(minOperations(91))     # 23
print(minOperations(92))     # 23
print(minOperations(93))     # 31
print(minOperations(94))     # 47
print(minOperations(95))     # 24
print(minOperations(96))     # 14
print(minOperations(97))     # 97
print(minOperations(98))     # 49
print(minOperations(99))     # 18
print(minOperations(100))    # 22