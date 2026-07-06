class InvalidAge(Exception):
    def __init__(self,age):
        self.age=age
        super().__init__("age should not be negative")

age=-2
try:
    if age<0:
        raise InvalidAge(age)
    print(f"the age is {age}")

except InvalidAge as e:
    print(e)