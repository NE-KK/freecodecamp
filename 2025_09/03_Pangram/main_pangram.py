# freecodecamp
# Daily Coding Challenges
# Day 24 (2025-09-03)
# Pangram

"""
Given a word or sentence and a string of lowercase letters, determine if the word or 
sentence uses all the letters from the given set at least once and no other letters.

Ignore non-alphabetical characters in the word or sentence.
Ignore letter casing in the word or sentence.
"""
import string
alphabet = string.ascii_lowercase


def compare_strings(string_base, string):
    result = True
    string_base = string_base.lower()
    string = string.lower()

    for letter in string_base:

        if letter in alphabet:
            if letter in string:
                continue
            else:
                result = False
                break
        else:
            continue

    return result


def is_pangram(sentence: str, letters: str) -> bool: 
    
    result = compare_strings(sentence, letters)
    
    if result:
        result = compare_strings(letters, sentence)


    return result
    

"""
print(is_pangram("hello", "helo"))
print(is_pangram("Hello World!", "helowrd"))
"""
