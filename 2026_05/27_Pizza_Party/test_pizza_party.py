from main_pizza_party import get_pizzas_to_order as gpo

# Test ----------------------------------------------------

print("Test 1: --------------------------------------------")
print(f"Ergebnis: {gpo([8, 8, 8])}")
print("Erwartet: 2")

print("Test 2: --------------------------------------------")
print(f"Ergebnis: {gpo([10, 9, 8, 2, 2, 6, 10])}")
print("Erwartet: 3")

print("Test 3: --------------------------------------------")
print(f"Ergebnis: {gpo([1, 2, 3, 4, 5])}")
print("Erwartet: 2")

print("Test 4: --------------------------------------------")
print(f"Ergebnis: {gpo([8, 8, 8, 8, 8, 8, 8, 8])}")
print("Erwartet: 3")

print("Test 5: --------------------------------------------")
print(f"Ergebnis: {gpo([9, 9, 6])}")
print("Erwartet: 1")

print("Test 6: --------------------------------------------")
print(f"Ergebnis: {gpo([10, 12, 16, 9, 8, 11, 15, 8, 0])}")
print("Erwartet: 5")
