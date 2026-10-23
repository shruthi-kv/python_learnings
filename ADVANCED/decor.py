
def decoratorFunction(fun):
    def wrapper():
        print("I'm about to execute a function")
        fun()
        print("I've executed a function")
    return wrapper

# def sayHello():
#     print("Hello")

# f = decoratorFunction(sayHello)
# f()
"""
def f():
    print("I'm about to execute a function")
    fun()
    print("I've executed a function")

"""



#alternat syntax for decorator
@decoratorFunction
def sayHello():
    print("Hello")

sayHello()