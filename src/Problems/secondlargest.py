a=[1,2,3,4,5,21]
largest=a[0]
second=a[0]
for i in a:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i

print(second)