# freecodecamp
# Daily Coding Challenges
# Day 6 (2025-08-16)
# Anagram Checker

"""
Given two strings, determine if they are anagrams of each other (contain the same characters in any order).

Ignore casing and white space.
"""

def count_chars(string: str) -> dict:
    char_dictionary = {}

    for char in string:
        if char in char_dictionary or char == " ":
            continue
        else:
            char_count = string.count(char)
            char_dictionary[char] = char_count

    return char_dictionary


def are_anagrams(str1: str, str2: str) -> bool:
    str1 = str1.lower()
    str2 = str2.lower()

    char_count_dictionary_1 = count_chars(str1)
    char_count_dictionary_2 = count_chars(str2)

    print(char_count_dictionary_1)
    print(char_count_dictionary_2)
    return char_count_dictionary_1 == char_count_dictionary_2
