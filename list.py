l1 = ['Raj',1632,12.25,'Patel',True]
l2 = ['python',1632,False]
print(l1)
print(l2)
print(l1[:3])
print(l2[1:])
print(l1 + l2)
print(l1*2)
l1[1] = 1234
print(l1)
del l1[1]
print(l1)

l1.append(1234)
print(l1)

l2 = l1.copy() 
print(l2)

l2.extend(l1)
print(l2)