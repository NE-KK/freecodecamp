# freecodecamp
# Daily Coding Challenges
# Day 21 (2025-09-01)
# Tribonacci Sequence

"""
The Tribonacci sequence is a series of numbers where each number is the sum of the three preceding ones. 
When starting with 0, 0 and 1, the first 10 numbers in the sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.

Given an array containing the first three numbers of a Tribonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.
- Your function should handle sequences of any length greater than or equal to zero.
- If the length is zero, return an empty array.
- Note that the starting numbers are part of the sequence.
"""

def tribonacci_sequence(start_sequence, length):
    result_sequence = []
    
    for i in range(length):
        if len(result_sequence) < 3:
            result_sequence.append(start_sequence[i])
        else:
            next_tribonacci = result_sequence[-1] + result_sequence[-2] + result_sequence[-3]
            result_sequence.append(next_tribonacci)

    return result_sequence

print(tribonacci_sequence([0, 0, 1], 20))