import random as r
print("float random number is ", r.random())
print("float random number through uniform is " ,r.uniform(10,99))
print(r.randint(0, 5))
print("random number",r.randrange(0,100,3))

name = ['raj','harsh','harshit','gunj','mohit']
print("Choice = ",r.choice(name))
print("Choices = ",r.choices(name,k=2))
print(name)
r.shuffle(name)
print(name)

city = ['bhavnagar','ahmedabad','surat','baroda']
print("sample = ",r.sample(city,k=2))