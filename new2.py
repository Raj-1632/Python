import random as r 
import string
def rand_pass(l=8):
    if l<4:
        print("Password must be minimum 8 characters.")

    # Uppercase letters
    uppercase_letters = list(string.ascii_uppercase)
    # Lowercase letters
    lowercase_letters = list(string.ascii_lowercase)
    # Digits 0–9
    digits = list(string.digits)
    # Special characters (includes punctuation like !@#$%^&*)
    special_characters = list(string.punctuation)

    pw = [ r.choice(uppercase_letters),r.choice(digits),r.choice(special_characters)]

    all_ch= uppercase_letters+lowercase_letters+digits+special_characters
    
    pw += r.choices(all_ch,k=(l-3))
    r.shuffle(pw)
    return "".join(pw)

len = int(input("Enter lenght : "))
print("pw is :",rand_pass(len))