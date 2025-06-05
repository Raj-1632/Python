l1 = ['Raj',1632,12.25,'Patel',True,1632]
l2 = ['python',1632,False]
l3 = [54,78,52,12,34,56,78,90]
l4 = ['e','r','g','v','j','p']

print("Index of 1632 in l1:",l1.index(1632))  # Find the index of 1632 in l1
print("Index of 1632 in l1:", l1.index(1632,2))  # Find the index of 2nd 1632 in l1

l1.append(1234)
print(l1)

l2 = l1.copy() 
print(l2)

l2.extend(l1)
print(l2)

l1.insert(1, 'inserted')
print(l1)

l1.pop(1)
print(l1)

l1.remove(True)
print(l1)

l1.reverse()
print(l1)

l3.sort()
print(l3)
print("Sorted l3:", sorted(l3))
print("Sorted l4:",sorted(l4))

print("Count of 78 in l3:", l3.count(78))

l2.clear()
print("After clearing l2:", l2)



