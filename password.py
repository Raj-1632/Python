import random as r
import string as s

def generate_password(length):
    
    if length < 4:
        print(" Password length must be at least 4.")
        
    elif length > 20:
        print(" Password length must be at most 20.")

    else:
        pw = [
            r.choice(s.ascii_uppercase),
            r.choice(s.ascii_lowercase),
            r.choice(s.digits),
            r.choice(s.punctuation)
        ]
 
        r.shuffle(pw)
        
        for i in range(length - 4):
            pw += [r.choice(s.ascii_uppercase + s.ascii_lowercase + s.digits + s.punctuation)]
        
        r.shuffle(pw)

        print("\n Password is",''.join(pw))
        print("\n Lenght of Password is",len(pw))

