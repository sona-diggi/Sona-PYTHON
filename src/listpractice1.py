a=int(input("enter the total number: "))
ls=list(map(int,input(f"enter the {a} numbers: ").split()))
summ=0
for i in range(a):
    summ=summ+ls[i]
print(summ)

