import random as r 
import string

def rand_pass(l=8):
    if l < 4:
        return "Password length must be at least 4."

    uppercase_letters = list(string.ascii_uppercase)
    lowercase_letters = list(string.ascii_lowercase)
    digits = list(string.digits)
    special_characters = list(string.punctuation)

    
    pw = [
        r.choice(uppercase_letters),
        r.choice(lowercase_letters),
        r.choice(digits),
        r.choice(special_characters)
    ]

    all_ch = uppercase_letters + lowercase_letters + digits + special_characters

    pw += r.choices(all_ch, k=(l - 4))
    r.shuffle(pw)

    return ''.join(pw)

length = int(input("Enter desired password length (min 4): "))
print("Generated Password:", rand_pass(length))


