import main_second_best as msb

if __name__ == "__main__":
    # test 1
    if msb.get_laptop_cost([1500, 2000, 1800, 1400], 1900) == 1800:
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")

    # test 2
    if msb.get_laptop_cost([1500, 2000, 2000, 1800, 1400], 1900) == 1800:
        print("Test 2: PASSED")
    else:
        print("Test 2: FAILED")

    # test 3
    if msb.get_laptop_cost([2099, 1599, 1899, 1499], 2200) == 1899:
        print("Test 3: PASSED")
    else:
        print("Test 3: FAILED")

    # test 4
    if msb.get_laptop_cost([2099, 1599, 1899, 1499], 1000) == 0:
        print("Test 4: PASSED")
    else:
        print("Test 4: FAILED")

    # test 5
    if msb.get_laptop_cost([1200, 1500, 1600, 1800, 1400, 2000], 1450) == 1400:
        print("Test 5: PASSED")
    else:
        print("Test 5: FAILED")