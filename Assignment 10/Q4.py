class Parent:
    def show(self):
        print("Parent class show method")

class Child(Parent):
    def show(self):
        print("Child class show method")

obj=Child()
obj.show()
obj1=Parent()
obj1.show()