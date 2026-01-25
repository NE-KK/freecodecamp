import main_vowel_balance

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

if __name__ == "__main__":
    # Test 1:
    if main_vowel_balance.is_balanced("racecar"):
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")

    # Test 2:
    if main_vowel_balance.is_balanced("Lorem Ipsum"):
        print("Test 2: PASSED")
    else:
        print("Test 2: FAILED")

    # Test 3:
    if not main_vowel_balance.is_balanced("Kitty Ipsum"):
        print("Test 3: PASSED")
    else:
        print("Test 3: FAILED")

    # Test 4:
    if not main_vowel_balance.is_balanced("string"):
        print("Test 4: PASSED")
    else:
        print("Test 4: FAILED")

    # Test 5:
    if main_vowel_balance.is_balanced(" "):
        print("Test 5: PASSED")
    else:
        print("Test 5: FAILED")

    # Test 6:
    if not main_vowel_balance.is_balanced("abcdefghijklmnopqrstuvwxyz"):
        print("Test 6: PASSED")
    else:
        print("Test 6: FAILED")

    # Test 7:
    if main_vowel_balance.is_balanced("123A#b!E&*456-o.U"):
        print("Test 7: PASSED")
    else:
        print("Test 7: FAILED")
