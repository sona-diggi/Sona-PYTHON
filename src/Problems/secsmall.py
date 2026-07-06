a=[5,3,8,2]
smallest=a[0] 
secsmall=a[0] 

for i in range(len(a)):
    if a[i]<smallest: 
        secsmall=smallest 
        smallest=a[i]
    elif a[i]>smallest and a[i]<secsmall:
        secsmall=a[i]
print(secsmall)