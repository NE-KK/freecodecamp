import main_strikes

"""
1. squares_with_three(1) should return 0.
2. squares_with_three(10) should return 1.
3. squares_with_three(100) should return 19.
4. squares_with_three(1000) should return 326.
5. squares_with_three(10000) should return 4531.
"""

if __name__ == "__main__":
    #Test 1
    if main_strikes.squares_with_three(1) == 0:
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")

    #Test 2
    if main_strikes.squares_with_three(10) == 1:
        print("Test 2: PASSED")
    else:
        print("Test 2: FAILED")

    #Test 3
    if main_strikes.squares_with_three(100) == 19:
        print("Test 3: PASSED")
    else:
        print("Test 3: FAILED")

    #Test 4
    if main_strikes.squares_with_three(1000) == 326:
        print("Test 4: PASSED")
    else:
        print("Test 4: FAILED")

    #Test 5
    if main_strikes.squares_with_three(10000) == 4531:
        print("Test 5: PASSED")
    else:
        print("Test 5: FAILED")
