# Inheritance

class A:
    def __init__(self, name):
        self.name = name

    def disp(self):
        print("Name is:", self.name)


'''
a = A("Aman")
a.disp()
'''


class B(A):
    def __init__(self, name, age):

        self.age = age
        A.__init__(self, name)

    def disp2(self):

        print("My name is", self.name)
        print("My age is", self.age)

'''b = B("aman",12)
b.disp()
b.disp2()
'''




# Multi level
class A:
    def __init__(self, name):
        self.name = name

    def disp(self):
        print("Name is:", self.name)


'''
a = A("Aman")
a.disp()
'''


class B(A):
    def __init__(self, name, age):

        self.age = age
        A.__init__(self, name)

    def disp2(self):

        print("My name is", self.name)
        print("My age is", self.age)

'''b = B("aman",12)
b.disp()
b.disp2()
'''
class C(B):
    def __init__(self, name, age, height):
        B.__init__(self, name,age)

    def disp3(self):
        print("My name is", self.name)
        print("My age is", self.age)
        print("My height is", self.age)

c = C("aman",12,4.5)
c.disp3()





# Inheritance

# Multi level
class A:
    def __init__(self, name):
        self.name = name

    def disp(self):
        print("Name is:", self.name)


'''
a = A("Aman")
a.disp()
'''


class B(A):
    def __init__(self, name, age):

        self.age = age
        A.__init__(self, name)

    def disp2(self):

        print("My name is", self.name)
        print("My age is", self.age)

'''b = B("aman",12)
b.disp()
b.disp2()
'''
class C(B):
    def __init__(self, name, age, height):
        B.__init__(self, name,age)

    def disp3(self):
        print("My name is", self.name)
        print("My age is", self.age)
        print("My height is", self.age)

c = C("aman",12,4.5)
c.disp3()













