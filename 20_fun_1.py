#with parameter without return
def fibonaci(number,a = 0,b = 1):
    next = b
    count = 0
    while count <= number:
        print(next)
        next = a + b
        a = b
        b = next
        count += 1

a = int(input("Enter a number : "))
fibonaci(a)