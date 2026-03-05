import main_factorializer

"""
1. factorial(0) should return 1.
2. factorial(5) should return 120.
3. factorial(20) should return 2432902008176640000.
"""


if __name__ == "__main__":
    # Test 1
    if main_factorializer.factorial(0) == 1:
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")

    # Test 2
    if main_factorializer.factorial(5) == 120:
        print("Test 2: PASSED")
    else:
        print("Test 2: FAILED")

    # Test 3
    if main_factorializer.factorial(20) == 2432902008176640000:
        print("Test 3: PASSED")
    else:
        print("Test 3: FAILED")

