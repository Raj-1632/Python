def fact(number):
    f = 1
    while number > 0:
        f = f * number
        number -= 1
    return f
        
a = int(input("Enter a number to find its factorial : "))
ans = fact(a)
print("Factorial of",a,"is",ans)