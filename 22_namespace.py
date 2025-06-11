str1 = "Raj"
str2 = "Patel"
str3 = ""
def concate(): 
    global str1,str2,str3 
    str3 = (str1 + str2) 
print(str1)
print(str2)
concate()
print(str3)
