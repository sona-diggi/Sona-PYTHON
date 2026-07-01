'''
a=list(map(int,input ("enter the number:").split()))
odd_count=0
even_count=0
for i in range(len(a)):
    if(a[i]%2!=0):
        odd_count+=1
    else:
        even_count+=1

print("odd_count: ",odd_count,"\n" ,"even_count: ",even_count)

'''

a=list(map(int,input ("enter the number:").split()))
odd_sum=0
even_sum=0
for i in range(len(a)):
    if(a[i]%2!=0):
        odd_sum=odd_sum+a[i]
    else:
        even_sum=even_sum+a[i]

print("odd_sum: ",odd_sum,"\n" ,"even_sum: ",even_sum)
