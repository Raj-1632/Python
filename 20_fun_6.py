def student(name,*marks):
    print("Student Name :",name)
    i = 0
    for mark in marks:
        print("Marks :",marks[i],"\n")
        i += 1
    
name = "Raj"
marks = 80,80,90,90
student(name,marks)