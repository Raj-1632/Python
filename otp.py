import random as r

def generate_otp(size):
    i = 1
    otp = ""
    for i in range(size):
        otp += str(r.randint(0,9))
    return otp