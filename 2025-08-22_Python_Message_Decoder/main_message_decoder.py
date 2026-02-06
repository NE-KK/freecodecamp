import string

"""
Given a secret message string, and an integer representing the number of letters that were used
to shift the message to encode it, return the decoded string.

- A positive number means the message was shifted forward in the alphabet.
- A negative number means the message was shifted backward in the alphabet.
- Case matters, decoded characters should retain the case of their encoded counterparts.
- Non-alphabetical characters should not get decoded.
"""

letters_lowercase = string.ascii_lowercase
letters_uppercase = string.ascii_uppercase


def decoded_letter(alphabet: str, letter:str, shift: int) -> str:
    letter_index = alphabet.index(letter)
    decoded_letter_index = letter_index - shift
    
    if decoded_letter_index > 25:
        decoded_letter_index -= 26

    letter_decoded = alphabet[decoded_letter_index]
    return letter_decoded


def decode(message: str, shift: int) -> str:
    decoded_message = ""

    for char in message:
        if char in letters_uppercase:
            decoded_message += decoded_letter(letters_uppercase, char, shift)
        elif char in letters_lowercase:
            decoded_message += decoded_letter(letters_lowercase, char, shift)
        else:
            decoded_message += char

    return decoded_message

"""
print(decode("Byffi Qilfx!", 20))      # Hello Woorld!
print(decode("Zqd xnt njzx?", -1))     # Are you okay?
"""