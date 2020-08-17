#required arguments

def takeInput(a,b):
    c= a+b
    print("sum =" + str(c))

takeInput(10,20)

#keyword args

def myInput(a,b):
    c= a+b
    print("sum =" + str(c))

myInput(a=100,b=200)

#default args
def defaultargs(a,b=100):
    c= a+b
    print("sum =" + str(c))

defaultargs(20,30)
defaultargs(20)