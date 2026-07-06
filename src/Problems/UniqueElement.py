a=[5,3,8,2,5,8]

for i in range(len(a)): 
    count=0
    for j in range(len(a)): 
        if a[i]==a[j]:
            count+=1
    if count==1:
        print(f"the {a[i]} has occured once")
    