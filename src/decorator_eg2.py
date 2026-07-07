def dec(fun):
    def wrap(a,b):
        if a<b:
            a,b=b,a
        return fun(a,b) 
    return wrap


#@dec
def add(a,b):
    print(a+b)

a=dec(add)
a(2,3)
#add(2,3)