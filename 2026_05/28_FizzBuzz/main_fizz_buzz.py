# freecodecamp
# Daily Coding Challenges
# Day 291 (2025-05-28)
# FizzBuzz Count

"""
Given a start and end number, count the number of fizz and buzz appearances in the range (inclusive).
    Numbers divisible by 3 count as a fizz.
    Numbers divisible by 5 count as a buzz.
    Numbers divisible by both 3 and 5 count as both a fizz and a buzz.

Return an object or dictionary with the counts in the format: { fizz, buzz }.
"""

def fizz_buzz_count(start, end):
    fizz_buzz_dict = {"fizz": 0, "buzz": 0}

    for i in range (start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizz_buzz_dict["fizz"] += 1
            fizz_buzz_dict["buzz"] += 1
            continue
        if i % 3 == 0:
            fizz_buzz_dict["fizz"] += 1

        if i % 5 == 0:
            fizz_buzz_dict["buzz"] += 1

    return fizz_buzz_dict
