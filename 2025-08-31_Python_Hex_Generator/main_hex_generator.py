# freecodecamp
# Daily Coding Challenges
# Day 20 (2025-08-31)
# Hex Generator

"""
Given a named CSS color string, generate a random hexadecimal (hex) color code that is dominant in the given color.

The function should handle "red", "green", or "blue" as an input argument.
If the input is not one of those, the function should return "Invalid color".
The function should return a random six-character hex color code where the input color value is greater than any of the others.
"""
from random import randint

# print(randint(0, 9))

def add_color():
    color = ""
    color += str(randint(0, 9))
    color += str(randint(0, 9))
    return color


def generate_hex(color):
    if color == 'red':
        color = 'FF'
        color += add_color()
        color += add_color()
    elif color == 'green':
        color = add_color()
        color += 'FF'
        color += add_color()
    elif color == 'blue':
        color = add_color()
        color += add_color()
        color += 'FF'
    else:
        color = "Invalid color" 

    return color

print(generate_hex('red'))
print(generate_hex('green'))
print(generate_hex('blue'))
print(generate_hex('yellow'))