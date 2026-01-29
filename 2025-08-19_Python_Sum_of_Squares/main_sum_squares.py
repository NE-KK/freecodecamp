# freecodecamp
# Daily Coding Challenges
# Day 9 (2025-08-19)
# Sum of squares

"""
Given a positive integer up to 1,000, return the sum of all the integers squared from 1 up to the number.
"""

def sum_of_squares(n):
    result = 0

    for i in range(1, n + 1):
        result += i**2

    return result

# print(sum_of_squares(5))