t1 = ('Raj',1632,12.25,'Patel',True,1632)
t2 = ('python',1632,False)
print(t1)
print(t2)
print(t1[3])
print(t1[:3])
print(t2[1:])
print(t1 + t2)
print(t1*2)
print(t1[-1])
t3 = (t1 + t2)
print(t3)

# Method & Functions

print(t1.count(1632))
print(t1.index(1632))
print(t1.index(1632,2))