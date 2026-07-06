a=[1,2,3,5,9,7,10]
largest=a[0] 
secLargest=a[0] 

for i in range(len(a)):
    if a[i]>largest:
        secLargest=largest
        largest =a[i]
    elif a[i]<largest and a[i]>secLargest:
        secLargest=a[i]
print(secLargest)