a=1234
product=1
while(a>0):
    last=a%10
    product=product*last
    a=a//10
print(product)