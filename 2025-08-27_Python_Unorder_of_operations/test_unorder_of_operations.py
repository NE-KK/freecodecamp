import main_unorder_of_operations as muo

if __name__ == "__main__":
    # test 1
    if muo.evaluate([5, 6, 7, 8, 9], ['+', '-']) == 3:
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")

    # test 2
    if muo.evaluate([17, 61, 40, 24, 38, 14], ['+', '%']) == 38:
        print("Test 2: PASSED")
    else:
        print("Test 2: FAILED")

    # test 3
    if muo.evaluate([20, 2, 4, 24, 12, 3], ['*', '/']) == 60:
        print("Test 3: PASSED")
    else:
        print("Test 3: FAILED")

    # test 4
    if muo.evaluate([11, 4, 10, 17, 2], ['*', '*', '%']) == 30:
        print("Test 4: PASSED")
    else:
        print("Test 4: FAILED")

    # test 5
    if muo.evaluate([33, 11, 29, 13], ['/', '-']) == -2:
        print("Test 5: PASSED")
    else:
        print("Test 5: FAILED")
