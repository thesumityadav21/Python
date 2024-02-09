# Destructor
# __del__()

class test:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Destructed")

    def disp(self):
        print("Name", self.name)


obj = test("rahul")
obj.disp()
obj1 = test("Raj")
obj1.disp()
