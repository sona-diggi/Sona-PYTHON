square=lambda x :x*x
print(square(2))

print(type(square))

add=lambda a,b :a+b
print(add(1,2))

even=lambda a :a%2==0
print(even(2))

#if else

even=lambda a: "even" if a%2==0 else "odd"
print(even(4))


students = [
    ("Ram",50),
    ("Sita",90),
    ("Kumar",75)
]

print(sorted(students, key=lambda x:x[0]))