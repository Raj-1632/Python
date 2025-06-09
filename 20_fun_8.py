a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

x = lambda a,b : a + b
print(x(a,b))

x = lambda a,b : a * b
print(x(a,b))

x = lambda a,b : a - b
print(x(a,b))

x = lambda a,b : a / b
print(x(a,b))