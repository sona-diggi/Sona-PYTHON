a=153
b=a
lenth=len(str(a))
val=0

while b>0:
    digit=b%10
    val=val+digit**lenth
    b=b//10
if (a==val):
    print("armstrong")

    
