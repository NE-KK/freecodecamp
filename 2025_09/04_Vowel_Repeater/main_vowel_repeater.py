# freecodecamp
# Daily Coding Challenges
# Day 25 (2025-09-04)
# Vowel Repeater

"""
Given a string, return a new version of the string where each vowel is duplicated one more time than the previous vowel you encountered. 
For instance, the first vowel in the sentence should remain unchanged. The second vowel should appear twice in a row. 
The third vowel should appear three times in a row, and so on.

- The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
- The original vowel should keeps its case.
- Repeated vowels should be lowercase.
- All non-vowel characters should keep their original case.
"""

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

def repeat_vowels(text):
    vowel_text = ""
    vowel_counter: int = 0
    
    for letter in text:
        if letter in vowels:
            vowel_text += letter + (letter.lower() * vowel_counter)
            vowel_counter += 1
        else:
            vowel_text += letter
   
    return vowel_text

print(repeat_vowels("hello world"))
"helloo wooorld"
print(repeat_vowels("AEIOU"))
"AEeIiiOoooUuuuu"
