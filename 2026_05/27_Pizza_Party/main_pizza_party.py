# freecodecamp
# Daily Coding Challenges
# Day 290 (2026-05-27)
# Pizza Party

"""
Given an array of hours worked today per person, return the number of pizzas to order for a pizza party.

    Divide each person's hours worked by 3 to get their slice count.
    You can't eat a partial slice, so round each person's slice count up to the nearest whole number.
    Each person gets a minimum of two slices.
    Each pizza has 8 slices. Round the total number of pizzas up to the nearest whole pizza.
"""

from math import ceil

def get_pizzas_to_order(hours_worked):
    pizzas_to_order = 0
    sum_pizza_slices = 0

    for hours in hours_worked:
        pizza_slices = ceil(hours / 3)

        if pizza_slices < 2:
            pizza_slices = 2

        sum_pizza_slices += pizza_slices


    pizzas_to_order = ceil((sum_pizza_slices / 8))

    return pizzas_to_order
