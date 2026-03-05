# freecodecamp
# Daily Coding Challenges
# Day 3 (2025-08-13)
# Fibonacci Sequence

"""
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. When starting with 0 and 1, 
the first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

Given an array containing the first two numbers of a Fibonacci sequence, and an integer representing the length of the sequence, 
return an array containing the sequence of the given length.

Your function should handle sequences of any length greater than or equal to zero.
If the length is zero, return an empty array.
Note that the starting numbers are part of the sequence.
"""

def fibonacci_sequence(start_sequence, length):
    fibonacci_list = []
    counter = 0

    for _ in range(length):
    
        if counter < 2:
            fibonacci_list.append(start_sequence[counter])
        else:
            next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_fibonacci)

        counter += 1


    return fibonacci_list
