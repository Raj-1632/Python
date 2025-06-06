d1 = {
    'name' : 'Raj',
    'age' : 20,
    'city' : 'Bhavnagar'
}
print(d1)
print(d1['name'])
print(d1['age'])
print(d1['city'])
d1['name'] = 'Raj Patel'
d1['no'] = 8282828282
print(d1)
del d1['no']
print(d1)

d2 = {}
print(d2)
d2['name'] = 'Raj'
d2['age'] = 20
d2['city'] = 'Bhavnagar'
print(d2)

d1['sub'] = ['Oracle','NS','Java','Python']
d1['topic'] = (1,2,3,4,5)
print(d1)

d2 = d1.copy()
print(d2)

print(d1.items())
print(d1.keys())
print(d1.values())

del d2['sub']
print(d2)
del d2['topic']
print(d2)
d2.clear()

print(d2)
d2 = d1.copy()
print(d2)

d2 = {}
d2['name'] = 'Raj'
d2['age'] = 20
d2['city'] = 'Bhavnagar'

print(d2.pop('name'))
print(d2)

print(d2.pop('age',20))
print(d2)

print(d2.popitem())
print(d2)

d2.clear()

print(d2)