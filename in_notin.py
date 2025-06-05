a = int(input(" Enter First Number : "))
b = int(input(" Enter Second Number : "))

print("\n",a,"is in list =",a in [1,2,3,4,5])
print(b,"is in list =",b in [1,2,3,4,5])

print("\n",a,"is not in list =",a not in [1,2,3,4,5])
print(b,"is not in list =",b not in [1,2,3,4,5])

name = input("Enter Your Name: ")
names = ["Raj","Harsh","Harshit","Gunj","Mohit"]
print(name in names)
print(name not in names)