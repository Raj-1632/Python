import random as r
name = "RajPatel"

print(" isalnum = ",str.isalnum(name))
print(" isalpha = ",str.isalpha(name))
print(" islower = ",str.islower(name))
print(" isnumeric = ",str.isnumeric(name))
print(" isspace = ",str.isspace(name))
print(" istitle = ",str.istitle(name))
print(" isupper = ",str.isupper(name))

city = ['bhavnagar','ahmedabad','surat','baroda']
print(""," - ".join(city))
r.shuffle(city)
print(city)
name = "Raj Patel"
print(" Replace = ",str.replace(name,"Raj","Harsh"))
print(" Replace = ",str.replace(name,"a","A",1))
print(" Split = ",str.split(name))