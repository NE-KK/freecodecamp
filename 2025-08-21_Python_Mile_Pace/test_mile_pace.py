import main_mile_pace

"""
1. mile_pace(3, "24:00") should return "08:00".
2. mile_pace(1, "06:45") should return "06:45".
3. mile_pace(2, "07:00") should return "03:30".
4. mile_pace(26.2, "120:35") should return "04:36".
"""

if __name__ == "__main__":
    # Test 1
    if main_mile_pace.mile_pace(3, "24:00") == "08:00":
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")

    # Test 2
    if main_mile_pace.mile_pace(1, "06:45") == "06:45":
        print("Test 2: PASSED")
    else:
        print("Test 2: FAILED")

    # Test 3
    if main_mile_pace.mile_pace(2, "07:00") == "03:30":
        print("Test 3: PASSED")
    else:
        print("Test 3: FAILED")

    # Test 4
    if main_mile_pace.mile_pace(26.2, "120:35") == "04:36":
        print("Test 4: PASSED")
    else:
        print("Test 4: FAILED")
