from functools import reduce 

aa=[1,2,3,4,5]

print(list(map(lambda a: a+5,aa)))
print(list(filter(lambda a:a if a >3 else 0,aa)))
print(list(filter(lambda a: a%2==0 ,aa)))
print(reduce(lambda a,b:a+b ,aa))


