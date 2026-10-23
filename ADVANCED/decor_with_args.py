
def repeatDecorator(n):
    def recorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return recorator



@repeatDecorator(7)
def sayHello(a):
    print(f"Hello {a}")

sayHello("Mac")