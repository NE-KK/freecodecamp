# freecodecamp
# Daily Coding Challenges
# Day 8 (2025-08-18)
# Factorializer

"""
Given an integer from zero to 20, return the factorial of that number. 
The factorial of a number is the product of all the numbers between 1 and the given number.

The factorial of zero is 1.
"""

def factorial(n):
    result = 1

    for i in range(1 ,n + 1):
        result *= i

    return result

# print(factorial(0))
