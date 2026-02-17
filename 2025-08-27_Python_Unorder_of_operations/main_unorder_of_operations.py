# freecodecamp
# Daily Coding Challenges
# Day 17 (2025-08-27)
# Unorder of Operations

"""
Given an array of integers and an array of string operators, apply the operations to the numbers sequentially from left-to-right. 
Repeat the operations as needed until all numbers are used. Return the final result.

For example, given [1, 2, 3, 4, 5] and ['+', '*'], return the result of evaluating 1 + 2 * 3 + 4 * 5 from left-to-right ignoring standard order of operations.

Valid operators are +, -, *, /, and %.
"""


def evaluate(numbers, operators):
    result = numbers[0]
    index_operator = 0

    for i in range(1, len(numbers)):
        if index_operator >= len(operators):
            index_operator = 0

        result = eval(str(result) + operators[index_operator] + str(numbers[i]))
        index_operator += 1

    return result
