name="sona"
rev=""

for ch in name:
    rev=ch+rev
if name==rev:
    print("palindrome")

num =121
temp=num

rev=0

while temp>0:
    last=last%10
    rev=rev*10+last
    temp=temp//10
if (rev==num):
    print("palindrom")
else:
    print("not a palindrome ")