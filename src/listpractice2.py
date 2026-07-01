#largest number

a=int(input("enter the total number: "))
ls=list(map(int,input(f"enter the {a} numbers: ").split()))

#Mistake : Initializing largest to 0
#largest=0
largest=ls[0]
for i in range(a):
    if(ls[i]>largest):
        largest =ls[i]

print(largest)