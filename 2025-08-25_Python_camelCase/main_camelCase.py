# freecodecamp
# Daily Coding Challenges
# Day 15 (2025-08-25)
# camelCase

"""
Given a string, return its camel case version using the following rules:

- Words in the string argument are separated by one or more characters from the following set: space ( ), dash (-), or underscore (_). Treat any sequence of these as a word break.
- The first word should be all lowercase.
- Each subsequent word should start with an uppercase letter, with the rest of it lowercase.
- All spaces and separators should be removed.
"""

import string
alphabet = string.ascii_letters


def to_camel_case(s):
    next_letter_uppercase = False
    camelCase_string = ""

    for char in s:
        if char in alphabet:
            if next_letter_uppercase:
                camelCase_string += char.upper()
                next_letter_uppercase = False
            else:
                camelCase_string += char.lower()
            
        else:
            next_letter_uppercase = True
            continue

    return camelCase_string
