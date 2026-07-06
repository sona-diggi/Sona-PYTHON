#without decorator

def decorator(func):
    print("decorator start")
    def wrap():
        func()
        print("inner wrap")
    return wrap

def greet():
    print("hello")

a=decorator(greet)
a()

#with decorator


def decorator(func):
    print("decorator start")
    def wrap():
        func()
        print("inner wrap")
    return wrap

@decorator
def greet():
    print("hello")

greet()
