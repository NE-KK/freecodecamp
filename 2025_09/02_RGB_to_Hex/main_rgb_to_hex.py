# freecodecamp
# Daily Coding Challenges
# Day 23 (2025-09-02)
# RGB to Hex

"""
Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.

Here are some example outputs for a given input:
"rgb(255, 255, 255)"    --  "#ffffff"
"rgb(1, 2, 3)"          --  "#010203"

Make any letters lowercase.
Return a # followed by six characters. Don't use any shorthand values.
"""

def create_rgb_list(rgb_str: str) -> list:
    rgb_str = rgb_str.lstrip("rgb(")
    rgb_str = rgb_str.rstrip(")")

    rgb_list = rgb_str.split(", ")
    rgb_list = [int(x) for x in rgb_list]

    return rgb_list


def create_hex_string(rgb_list: list) -> str:
    hex_string = "#"
    
    for i in rgb_list:
        hex_num = hex(i).lstrip("0x")
        hex_num = hex_num.zfill(2)
        hex_string += hex_num

    return hex_string


def rgb_to_hex(rgb):
    rgb_list = create_rgb_list(rgb)
    hex_string = create_hex_string(rgb_list)

    return hex_string

"""
print(rgb_to_hex("rgb(255, 255, 255)"))
print(rgb_to_hex("rgb(1, 2, 3)"))
"""