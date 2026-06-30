#2 types of variables


#local

def fun1():
    a=5
    print(a)
fun1()
a=6
print(a)

#global 
ab=4
def fun():
    print(ab)
fun()
print(ab)

#using global keyword

ac=4
def fun2():
    global ac
    ac=5
    print(ac)
fun2()
print(ac)