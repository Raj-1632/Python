n = int(input("Enter N number : "))
i = 1
count = 0
for i in range(n):
    if (i % 2 != 0):
        count += i

print("Sum of odd numbers : ",count)
