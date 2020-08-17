#no args function
def sample():
    "Author: Anuvrat Kumar Singh"
    print("hello anuvrat")
    print("\nmultiline")
    return

sample()

#function with args and no return value

def sum(a,b):
    c=a + b
    print("Sum of two number is ->" + str(c))

sum(50,50)

# function with args and return value
def multiply(a,b):
    c = a * b
    return c
def add(a,b):
    c= a + b
    print(c)


x = multiply(4,20)
add(x,10)

#function with no arg and return value

def myfunc():
    a= 10
    return a

print(str(myfunc()))