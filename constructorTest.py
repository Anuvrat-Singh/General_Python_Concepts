"step1: create a class"

class firstClass:
    "function with class scope"
    def __init__(self, a, b):
        print("constructor chacha. object created")
        print("a= " + str(a))
        print("b= " + str(b))


    def myfunc(self):
        print("my first class")

# commenting to call this class in another class. uncommenting and running will also work fine
#a= firstClass(10,20)
#a.myfunc()