# freecodecamp
# Daily Coding Challenges
# Day 7 (2025-08-17)
# Targeted Sum

"""
Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. 
Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.

The returned array should have the indices in ascending order.
"""

def find_target(arr: list, target: int):
    # result = "Target not found"
    result = []

    for i in range(len(arr)):     
        for j in range(i + 1 , len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]

    return "Target not found"
