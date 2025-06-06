n1 = int(input(" Enter first number : "))
n2 = int(input(" Enter second number : "))
n3 = int(input(" Enter third number : "))
n4 = int(input(" Enter fourth number : "))

print("\n",n1,"-",n2,"and",n3,"-",n4,"are equal =",(n1 == n2 and n3 == n4))
print("",n1,"-",n2,"or",n3,"-",n4,"are equal =",(n1 == n2 or n3 == n4))
print("",n1,"-",n2,"and",n3,"-",n4,"are not equal =",not(n1 == n2 and n3 == n4))