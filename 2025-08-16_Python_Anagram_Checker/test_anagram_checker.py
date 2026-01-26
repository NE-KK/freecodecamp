import main_anagram_checker

"""
1. are_anagrams("listen", "silent") should return true.
2. are_anagrams("School master", "The classroom") should return true.
3. are_anagrams("A gentleman", "Elegant man") should return true.
4. are_anagrams("Hello", "World") should return false.
5. are_anagrams("apple", "banana") should return false.
6. are_anagrams("cat", "dog") should return false.
"""

if __name__ == "__main__":
    print("Test")

    # Test 1
    if main_anagram_checker.are_anagrams("listen", "silent"):
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")

    # Test 2
    if main_anagram_checker.are_anagrams("School master", "The classroom"):
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")

    # Test 3
    if main_anagram_checker.are_anagrams("A gentleman", "Elegant man"):
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")

    # Test 4
    if not main_anagram_checker.are_anagrams("Hello", "World"):
        print("Test 6: PASSED")
    else:
        print("Test 6: FAILED")

    # Test 5
    if not main_anagram_checker.are_anagrams("apple", "banana"):
        print("Test 6: PASSED")
    else:
        print("Test 6: FAILED")

    # Test 6
    if not main_anagram_checker.are_anagrams("cat", "dog"):
        print("Test 6: PASSED")
    else:
        print("Test 6: FAILED")