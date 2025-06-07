#without parameter with return 
import random

def quote():
    quotes = [
        "Believe in yourself!",
        "Push yourself, because no one else is going to do it for you.",
        "Success doesn’t just find you. You have to go out and get it.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it."
    ]
    return random.choice(quotes)

quote = quote()
print("Motivational Quote:", quote)
