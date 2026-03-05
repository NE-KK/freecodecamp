import main_targeted_sum

"""
1. find_target([2, 7, 11, 15], 9) should return [0, 1].
2. find_target([3, 2, 4, 5], 6) should return [1, 2].
3. find_target([1, 3, 5, 6, 7, 8], 15) should return [4, 5].
4. find_target([1, 3, 5, 7], 14) should return 'Target not found'.
"""

if __name__ == "__main__":
    # Test 1
    if main_targeted_sum.find_target([2, 7, 11, 15], 9) == [0, 1]:
        print("Test1: PASSED")
    else:
        print("Test1: FAILED")

    # Test 2
    if main_targeted_sum.find_target([3, 2, 4, 5], 6) == [1, 2]:
        print("Test2: PASSED")
    else:
        print("Test2: FAILED")

    # Test 3
    if main_targeted_sum.find_target([1, 3, 5, 6, 7, 8], 15) == [4, 5]:
        print("Test3: PASSED")
    else:
        print("Test3: FAILED")
    
    # Test 4
    if main_targeted_sum.find_target([1, 3, 5, 7], 14) == 'Target not found':
        print("Test4: PASSED")
    else:
        print("Test4: FAILED")