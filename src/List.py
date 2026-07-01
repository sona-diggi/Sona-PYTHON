numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])

#Omitting start
numbers = [10, 20, 30, 40, 50]

print(numbers[:3])

#Omitting stop
numbers = [10, 20, 30, 40, 50]

print(numbers[2])

#Omitting start
numbers = [10, 20, 30, 40, 50]

print(numbers[:])


#understanding copy

a=[10,20,30]
b=a
b[0]=100
print(a)
print(b)

numbers = [10, 20, 30]
numbers.insert(2,40)
print(numbers)

numbers = [10, 20, 30]
numbers.insert(-1,50)
print(numbers)
