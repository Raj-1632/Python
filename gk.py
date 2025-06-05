l1 = ['Raj',12.25,'Patel',1632,True,1632]
l2 = ['python',1632,False]

#First Method
print(" By First Method : ",l1.index(1632,2))

#Second Method

i1 = l1.index(1632)

i2 = l1.index(1632,i1+1)
print(" By Second Method : ",i2)