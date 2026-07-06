def outer():
    print("outer function")

    def inner():
        print("inner function")
    return inner
result = outer()
result()
