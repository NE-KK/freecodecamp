import main_candlelight as mc

if __name__ == "__main__":
    # test 1
    if mc.burn_candles(7, 2) == 13:
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")

    # test 2
    if mc.burn_candles(10, 5) == 12:
        print("Test 2: PASSED")
    else:
        print("Test 2: FAILED")

    # test 3
    if mc.burn_candles(20, 3) == 29:
        print("Test 3: PASSED")
    else:
        print("Test 3: FAILED")

    # test 4
    if mc.burn_candles(17, 4) == 22:
        print("Test 4: PASSED")
    else:
        print("Test 4: FAILED")

    # test 5
    if mc.burn_candles(2345, 3) == 3517:
        print("Test 5: PASSED")
    else:
        print("Test 5: FAILED")