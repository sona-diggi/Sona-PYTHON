a=[5,3,8,2,5,8]
for i in range (len(a)):
    count=1
    found=False
    for k in range(i):
        if a[i]==a[k]:
            found=True
            break
    
    if found==False:
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                count+=1
        print(f"{a[i]},has occured,{count},times")


'''
a=[5,3,8,2,5,8]
for i in range (len(a)):
    count=1
    for k in range(i):
        if a[i]==a[k]:
            break
    
    else:    
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                count+=1
        print(f"{a[i]},has occured,{count},times")
    
'''

'''
a = [5, 3, 8, 2, 5, 8]

freq = {}

for num in a:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key in freq:
    print(key, "occurs", freq[key], "times")
'''