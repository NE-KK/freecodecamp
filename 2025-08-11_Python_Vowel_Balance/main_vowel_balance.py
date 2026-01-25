# freecodecamp
# Daily Coding Challenges
# Day 1 (2025-08-11)
# Vowel Balance
"""
Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.
Vowels are: a, A, e, E, i, I, o, O, u, U
If there's an odd number of characters in the string, ignore the center character.
examples:
    1. is_balanced("racecar") should return True.
    2. is_balanced("Lorem Ipsum") should return True.
    3. is_balanced("Kitty Ipsum") should return False.
    4. is_balanced("string") should return False.
    5. is_balanced(" ") should return True.
    6. is_balanced("abcdefghijklmnopqrstuvwxyz") should return False.
    7. is_balanced("123A#b!E&*456-o.U") should return True.
"""


def count_vowels(string):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count



def is_balanced(s):
    half_count = int(len(s) / 2)
    string_one = s[0:half_count]
    
    if len(s) % 2 == 0:
        string_two = s[half_count:]
    else:
        string_two = s[half_count+1:]

    vowel_count_string_one = count_vowels(string_one)
    vowel_count_string_two = count_vowels(string_two)

    # for debugging --------------------------------------------
    # print(string_one)
    # print(string_two)
    # print(vowel_count_string_one)
    # print(vowel_count_string_one)
    
    return vowel_count_string_one == vowel_count_string_two
