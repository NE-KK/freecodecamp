import main_sum_squares

"""
1. sum_of_squares(5) should return 55.
2. sum_of_squares(10) should return 385.
3. sum_of_squares(25) should return 5525.
4. sum_of_squares(500) should return 41791750.
5. sum_of_squares(1000) should return 333833500.
"""

if __name__ == "__main__":
    # Test 1
    if main_sum_squares.sum_of_squares(5) == 55:
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")

    # Test 2
    if main_sum_squares.sum_of_squares(10) == 385:
        print("Test 2: PASSED")
    else:
        print("Test 2: FAILED")

    # Test 3
    if main_sum_squares.sum_of_squares(25) == 5525:
        print("Test 3: PASSED")
    else:
        print("Test 3: FAILED")

    # Test 4
    if main_sum_squares.sum_of_squares(500) == 41791750:
        print("Test 4: PASSED")
    else:
        print("Test 4: FAILED")

    # Test 5
    if main_sum_squares.sum_of_squares(1000) == 333833500:
        print("Test 5: PASSED")
    else:
        print("Test 5: FAILED")
