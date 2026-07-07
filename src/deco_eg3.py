def upper(fun):
    def wrap(*word):
        word=word.upper()
        return fun(*word)
    return wrap


def f1(word):
    print(word)
    
a=upper(f1)
a("hello","how are you")

#f1("hello")