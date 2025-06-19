import random as r 
import string
def rand_pass(l=8):
    if l<4:
        print("Password must be minimum 8 characters.")

   
    uppercase_letters = list(string.ascii_uppercase)
    
    lowercase_letters = list(string.ascii_lowercase)
   
    digits = list(string.digits)
    
    special_characters = list(string.punctuation)

    pw = [ r.choice(uppercase_letters),r.choice(lowercase_letters),r.choice(digits),r.choice(special_characters)]

    print(pw)

    all_ch = uppercase_letters+lowercase_letters+digits+special_characters

    pw = pw+r.choices(all_ch,k= (l-4))

    r.shuffle(pw)

    print("\n Password is ",''.join(pw))

