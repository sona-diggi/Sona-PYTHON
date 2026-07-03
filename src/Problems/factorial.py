#without recursion
'''
a=5
fact=1

for i in range(1,a+1):
    fact=i*fact
print(fact)

'''


def fun(a):
    if a==1:
        return 1
    else:
        return a* fun(a-1)
print(fun(4))
