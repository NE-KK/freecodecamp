# freecodecamp
# Daily Coding Challenges
# Day 14 (2025-08-24)
# Character Battle

"""
 two strings representing your army and an opposing army, each character from your army battles the character at the same position from the opposing army using the following rules:

- Characters a-z have a strength of 1-26, respectively.
- Characters A-Z have a strength of 27-52, respectively.
- Digits 0-9 have a strength of their face value.
- All other characters have a value of zero.
- Each character can only fight one battle.
"""

import string
alphabet = string.ascii_letters
numbers = string.digits


def calculate_strength(army: str) -> int:
    for char in army:
        if char in numbers:
            return int(char)
        elif char in alphabet:
            return alphabet.index(char) + 1
        else:
            return 0 


def battle_calculation(my_army: str, opposing_army: str) -> list:
    my_wins = 0
    opposing_wins = 0

    for i in range(len(my_army)):
        my_strength = calculate_strength(my_army[i])
        opponent_strength = calculate_strength(opposing_army[i])

        if my_strength > opponent_strength:
            my_wins += 1
        elif my_strength < opponent_strength:
            opposing_wins += 1
        else:
            continue
    
    return [my_wins, opposing_wins]


def battle_result(my_army: str, opposing_army: str) -> str:
    battle_list = battle_calculation(my_army, opposing_army)
    my_army_wins = battle_list[0]
    opposing_army_wins = battle_list[1]

    if my_army_wins > opposing_army_wins:
        return "We won"
    elif my_army_wins < opposing_army_wins:
        return "We lost"
    else:
        return "It was a tie"


def battle(my_army: str, opposing_army: str) -> str:
    result = ""
    
    if len(my_army) > len(opposing_army):
        result = "Opponent retreated"
    elif len(my_army) < len(opposing_army):
        result = "We retreated"
    else:
        result = battle_result(my_army, opposing_army)

    return result
