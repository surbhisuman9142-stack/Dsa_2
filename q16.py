#__init__()constructor
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1 = student("surbhi",21)
s2 = student("bishal",23)
print(s1.name)
print(s2.age)