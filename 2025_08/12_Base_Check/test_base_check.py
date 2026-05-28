import main_base_check

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

if __name__ == "__main__":
    # Test 1
    if main_base_check.is_valid_number("10101", 2):
        print("Test 01: PASSED")
    else:
        print("Test 01: FAILED")       
    
    # Test 2
    if not main_base_check.is_valid_number("10201", 2):
        print("Test 02: PASSED")
    else:
        print("Test 02: FAILED")       
    
    # Test 3
    if main_base_check.is_valid_number("76543210", 8):
        print("Test 03: PASSED")
    else:
        print("Test 03: FAILED")   

    # Test 4
    if not main_base_check.is_valid_number("9876543210", 8):
        print("Test 04: PASSED")
    else:
        print("Test 04: FAILED")   

    # Test 5
    if main_base_check.is_valid_number("9876543210", 10):
        print("Test 05: PASSED")
    else:
        print("Test 05: FAILED")

    # Test 6
    if not main_base_check.is_valid_number("ABC", 10):
        print("Test 06: PASSED")
    else:
        print("Test 06: FAILED")

    # Test 7
    if main_base_check.is_valid_number("ABC", 16):
        print("Test 07: PASSED")
    else:
        print("Test 07: FAILED")

    # Test 8
    if main_base_check.is_valid_number("Z", 36):
        print("Test 08: PASSED")
    else:
        print("Test 08: FAILED")

    # Test 9
    if main_base_check.is_valid_number("ABC", 20):
        print("Test 09: PASSED")
    else:
        print("Test 09: FAILED")

    # Test 10
    if main_base_check.is_valid_number("4B4BA9", 16):
        print("Test 10: PASSED")
    else:
        print("Test 10: FAILED")

    # Test 11
    if not main_base_check.is_valid_number("5G3F8F", 16):
        print("Test 11: PASSED")
    else:
        print("Test 11: FAILED")

    # Test 12
    if main_base_check.is_valid_number("5G3F8F", 17):
        print("Test 12: PASSED")
    else:
        print("Test 12: FAILED")

    # Test 13
    if not main_base_check.is_valid_number("abc", 10):
        print("Test 13: PASSED")
    else:
        print("Test 13: FAILED")

    # Test 14
    if main_base_check.is_valid_number("abc", 16):
        print("Test 14: PASSED")
    else:
        print("Test 14: FAILED")

    # Test 15
    if main_base_check.is_valid_number("AbC", 16):
        print("Test 15: PASSED")
    else:
        print("Test 15: FAILED")

    # Test 16
    if main_base_check.is_valid_number("z", 36):
        print("Test 16: PASSED")
    else:
        print("Test 16: FAILED")
