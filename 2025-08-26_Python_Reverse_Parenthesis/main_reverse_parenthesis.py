# freecodecamp
# Daily Coding Challenges
# Day 16 (2025-08-26)
# Reverse Parenthesis

"""
Given a string that contains properly nested parentheses, return the decoded version of the string using the following rules:

- All characters inside each pair of parentheses should be reversed.
- Parentheses should be removed from the final result.
- If parentheses are nested, the innermost pair should be reversed first, and then its result should be included in the reversal of the outer pair.
- Assume all parentheses are evenly balanced and correctly nested.
"""


def find_open_par(start: int, s: str) -> int:
    index = -1
    for i in range(0, start, 1):
        if s[i] == "(":
            index = i

    return index


def partial_reverse(start: int, end: int, s: str) -> str:
    sub_string = s[start + 1:end]
    
    return "".join(reversed(sub_string))


def built_string(start: int, end: int, s: str, sub_string: str) -> str:
    start_string = s[0:start]
    end_string = s[end+1::]
    
    return "".join(start_string + sub_string + end_string)


def decode(s: str) -> str:
    while "(" in s:
        index_end = s.find(")")
        index_start = find_open_par(index_end, s)
        sub_string = partial_reverse(index_start, index_end, s)
        s = built_string(index_start, index_end, s, sub_string)

    return s
