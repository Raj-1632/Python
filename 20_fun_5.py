def cal(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    mod = a % b
    return add,sub,mul,div,mod

a = int(input(" Enter First Number : "))
b = int(input(" Enter Second Number : "))
result = cal(a,b)

print(" Addition is",result[0])
print(" Subtraction is",result[1])
print(" Multiplcation is",result[2])
print(" Division is",result[3])
print(" Modulo is",result[4])