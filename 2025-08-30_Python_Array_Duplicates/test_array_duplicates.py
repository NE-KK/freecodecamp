import main_array_duplicates as mad

if __name__ == "__main__":
    # test 1
    if mad.find_duplicates([1, 2, 3, 4, 5]) == []:
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")

    # test 2
    if mad.find_duplicates([1, 2, 3, 4, 1, 2]) == [1, 2]:
        print("Test 2: PASSED")
    else:
        print("Test 2: FAILED")

    # test 3
    if mad.find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]) == [-6, 0, 2, 4, 5, 23]:
        print("Test 2: PASSED")
    else:
        print("Test 2: FAILED")
