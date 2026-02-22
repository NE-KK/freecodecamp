# freecodecamp
# Daily Coding Challenges
# Day 5 (2025-08-15)
# Jbelmud Text

"""
Given a string, return a jumbled version of that string where each word is transformed using the following constraints:

The first and last letters of the words remain in place
All letters between the first and last letter are sorted alphabetically.
The input strings will contain no punctuation, and will be entirely lowercase.
"""

def jbelmu(text):
    text_list = text.split()
    new_text_list = []
    new_text = ''

    for word in text_list:
        if len(word) > 3:
            word_list = list(word)
            word_part = word_list[1:-1]
            word_part.sort()

            word_part.insert(0, word_list[0])
            word_part.append(word_list[-1])

            word = ''.join(word_part)

        new_text += word + ' '

    new_text = new_text.strip()
    return new_text

