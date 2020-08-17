"step1: create a class"

class firstClass:
    "function with class scope"
    def myfunc(self):
        print("my first class")

obj1 = firstClass()     #thats how we create an object in python

#to call any member function use . operator like java
obj1.myfunc()

class newClass:
    "function with no args and no return"
    def hello(self):
        print("hello world")

    #func with arg and no return value
    def functionWithArgs(self,a,b):
        c= a+ b
        print("sum = "+ str(c))


    #func with args and return value
    def multiply(self,a,b):
        c=a*b
        return c

obj1 = newClass()

obj1.hello()

obj1.functionWithArgs(100,110)
x = obj1.multiply(2,3)
print(x)