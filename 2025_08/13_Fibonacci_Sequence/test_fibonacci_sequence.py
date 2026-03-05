import main_fibonacci_sequence

"""
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. When starting with 0 and 1, 
the first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

Given an array containing the first two numbers of a Fibonacci sequence, and an integer representing the length of the sequence, 
return an array containing the sequence of the given length.

Your function should handle sequences of any length greater than or equal to zero.
If the length is zero, return an empty array.
Note that the starting numbers are part of the sequence.
"""

if __name__ == "__main__":
    # Test 1
    result_sequence_1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
    if main_fibonacci_sequence.fibonacci_sequence([0, 1], 20) == result_sequence_1:
        print("Test 01: PASSED")
    else:
        print("Test 01: FAILED")    

    # Test 2
    result_sequence_2 = [21]
    if main_fibonacci_sequence.fibonacci_sequence([21, 32], 1) == result_sequence_2:
        print("Test 02: PASSED")
    else:
        print("Test 02: FAILED")  

    # Test 3
    result_sequence_3 = []
    if main_fibonacci_sequence.fibonacci_sequence([0, 1], 0) == result_sequence_3:
        print("Test 03: PASSED")
    else:
        print("Test 03: FAILED")  

    # Test 4
    result_sequence_4 = [10, 20]
    if main_fibonacci_sequence.fibonacci_sequence([10, 20], 2) == result_sequence_4:
        print("Test 04: PASSED")
    else:
        print("Test 04: FAILED")  

    # Test 5
    result_sequence_5 = [123456789, 987654321, 1111111110, 2098765431, 3209876541]
    if main_fibonacci_sequence.fibonacci_sequence([123456789, 987654321], 5) == result_sequence_5:
        print("Test 05: PASSED")
    else:
        print("Test 05: FAILED")  
