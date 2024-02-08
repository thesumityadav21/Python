# Encapsulation

class Animal:
    def __init__(self, name):
        self.name = name
        input(self.name)


class Dog(Animal):
    def __init__(self, name, age):
        self._age = age
        Animal.__init__(self, name)

class Puppy(Dog):
    def __init__( self,name, age, size):
        self.size = size
        Dog.__init__(self,name,age)


def disp(self):
        print(self.name)
        print(self.age)
        print(self.size)


obj = Puppy("ss",'d', 23)
obj.disp()
