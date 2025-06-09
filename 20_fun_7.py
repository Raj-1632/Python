def fac(a):
    if a == 1:
        return 1
    else:
        return (a * fac(a - 1))
    
a = int(input(" Enter Number for it's Factorial : "))
result = fac(a)
print(" The Factorial of",a,"is",result)