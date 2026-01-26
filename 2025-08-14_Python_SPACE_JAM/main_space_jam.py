# freecodecamp
# Daily Coding Challenges
# Day 4 (2025-08-14)
# S P A C E J A M

"""
Given a string, remove all spaces from the string, insert two spaces between every character, 
convert all alphabetical letters to uppercase, and return the result.

Non-alphabetical characters should remain unchanged (except for spaces).
"""

def space_jam(s):
    result_string = ""

    for char in s:
        if not char == " ":
            result_string += char.upper() + "  "

    result_string = result_string.strip()
    return result_string
