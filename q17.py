#methods
class student:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print("My name is",self.name)
s1 = student("surbhi")
s1.introduce()