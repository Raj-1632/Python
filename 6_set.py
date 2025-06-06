s1 = {'a','b','x'}
s2 = {'y','c','z'}
print(s1);print(s2)

s1.add('c')
s2.add('x')
print(s1);print(s2,"\n")

print("Intersection : ",s1.intersection(s2))
print("Union : ",s1.union(s2))
print("Difference : ",s1.difference(s2),"\n")

print("Intersection : ",s2.intersection(s1))
print("Union : ",s2.union(s1))
print("Difference : ",s2.difference(s1),"\n")

s1.remove('c')
s2.remove('x')
print(s1);print(s2)