# freecodecamp
# Daily Coding Challenges
# Day 13 (2025-08-23)
# Unnatural Prime

"""
Given an integer, determine if that number is a prime number or a negative prime number.

- A prime number is a positive integer greater than 1 that is only divisible by 1 and itself.
- A negative prime number is the negative version of a positive prime number.
- 1 and 0 are not considered prime numbers.
"""

def is_unnatural_prime(n):
    is_prime = True

    if n < 0:
        n *= -1

    if n < 2:
        is_prime = False

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
        
            break

    return is_prime
