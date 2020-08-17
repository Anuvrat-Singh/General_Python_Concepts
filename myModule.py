"module can consist of python's executeable code, functions, classes, functions in class "

# python executable code example

print("Lets understand what is module and how to use module. I'm in myModule")


def moduleFunc(a,b):
    print("This is a function in module")
    c= a + b
    return c


class moduleClass:
    def funcInsideClass(self):
        print("This is a function inside module of a class")