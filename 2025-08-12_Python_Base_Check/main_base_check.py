# freecodecamp
# Daily Coding Challenges
# Day 2 (2025-08-12)
# Base Check

"""
Given a string representing a number, and an integer base from 2 to 36, determine whether the number is valid in that base.

The string may contain integers, and uppercase or lowercase characters.
The check should be case-insensitive.
The base can be any number 2-36.
A number is valid if every character is a valid digit in the given base.
Example of valid digits for bases:
    Base 2: 0-1
    Base 8: 0-7
    Base 10: 0-9
    Base 16: 0-9 and A-F
    Base 36: 0-9 and A-Z
"""


def find_char_position(input_string):
    char_list = "0123456789abcdefghijklmnopqrstuvwxyz"
    char_pos_max = 0

    for char in input_string:
        char_pos_current = char_list.find(char.lower())

        if char_pos_current > char_pos_max:
            char_pos_max = char_pos_current

    return char_pos_max


def is_valid_number(n, base):
    rank = find_char_position(n)

    return base > rank
