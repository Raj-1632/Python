import random as r
import string as s

def generate_password(length):
    
    if length < 4:
        print(" Password length must be at least 4.")
        
    elif length > 20:
        print(" Password length must be at most 20.")

    else:
        password = [
            r.choice(s.ascii_uppercase),
            r.choice(s.ascii_lowercase),
            r.choice(s.digits),
            r.choice(s.punctuation)
        ]
 
        r.shuffle(password)
        
        for i in range(length - 4):
            password += [r.choice(s.ascii_uppercase + s.ascii_lowercase + s.digits + s.punctuation)]
        
        r.shuffle(password)
        generated_password = ''.join(password)
        print("\n Password is",generated_password)
        print("\n Lenght of Password is",len(password))
        save_password(generated_password)  # Call function to save password to file


def save_password(password):
    file_name = "generated_passwords.txt"
    with open(file_name, 'a') as file:  # 'a' for append mode
        file.write(password + '\n')
