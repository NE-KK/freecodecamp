# freecodecamp
# Daily Coding Challenges
# Day 20 (2025-08-30)
# Duplicates Array

"""
Array Duplicates
Given an array of integers, return an array of integers that appear more than once in the initial array, 
sorted in ascending order. If no values appear more than once, return an empty array.

Only include one instance of each value in the returned array.
"""

def find_duplicates(arr):
    duplicate_arr = []
    
    for i in arr:
        i_count = arr.count(i)

        if i_count > 1 and i not in duplicate_arr:
            duplicate_arr.append(i)
    
    duplicate_arr.sort()
    return duplicate_arr
