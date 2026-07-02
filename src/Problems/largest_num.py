a=[1,2,3,5,6,4,9,8]
largest=a[0]

for i in range(len(a)):
    if a[i]>largest:
        largest=a[i]
print(largest)
    
