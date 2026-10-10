class student:
    college = "ABC College"#class variable
    def __init__(self,name):#instance variable
        self.name = name
s1 = student("surbhi")
s2 = student("bishal")
print(s1.name)
print(s2.name)
print(s1.college)
print(s2.college)