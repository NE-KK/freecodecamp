# freecodecamp
# Daily Coding Challenges
# Day 18 (2025-08-28)
# Second Best

"""
Given an array of integers representing the price of different laptops, and an integer representing your budget, return:

1. The second most expensive laptop if it is within your budget, or
2. The most expensive laptop that is within your budget, or
3. 0 if no laptops are within your budget.

Duplicate prices should be ignored.
- If the most expensive laptop is in budget take the next cheaper one.
"""

def get_laptop_cost(laptops: int, budget: int) -> int:
    found = False
    price_my_laptop = 0
    price = max(laptops)
    laptops.remove(price)
    
    for _ in range(len(laptops)):
        price = max(laptops)
        if price < budget:
            found = True
            price_my_laptop = price
        else:
            laptops.remove(price)

    return price_my_laptop
