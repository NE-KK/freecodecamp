from main_fizz_buzz import fizz_buzz_count as fbc

"""
1. fizz_buzz_count(1, 11) should return {"fizz": 3, "buzz": 2}.
2. fizz_buzz_count(14, 41) should return {"fizz": 9, "buzz": 6}.
3. fizz_buzz_count(24, 100) should return {"fizz": 26, "buzz": 16}.
4. fizz_buzz_count(-635, -14) should return {"fizz": 207, "buzz": 125}.
5. fizz_buzz_count(-5432, 6789) should return {"fizz": 4074, "buzz": 2444}.
"""

# Tests-----------------------------------------
print("Test 1: ---------------------")
print(f"Ergebnis: {fbc(1, 11)}")
print("Erwartet: {'fizz': 3, 'buzz': 2}")

print("Test 2: ---------------------")
print(f"Ergebnis: {fbc(14, 41)}")
print("Erwartet: {'fizz': 9, 'buzz': 6}")

print("Test 3: ---------------------")
print(f"Ergebnis: {fbc(24, 100)}")
print("Erwartet: {'fizz': 26, 'buzz': 16}")

print("Test 4: ---------------------")
print(f"Ergebnis: {fbc(-635, -14)}")
print("Erwartet: {'fizz': 207, 'buzz': 125}")

print("Test 5: ---------------------")
print(f"Ergebnis: {fbc(-5432, 6789)}")
print("Erwartet: {'fizz': 4074, 'buzz': 2444}")
