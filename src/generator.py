def gen():
    yield "hello"
    print("sona")
    yield "hi"

give=gen()
print(next(give))
print(next(give))
print(next(give))