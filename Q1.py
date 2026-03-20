class Parent:
    def ParentClassMethod(self):
        print("Call from Parents")

class Child(Parent):
    def ChildClassMethod(self):
        print("Replied by Child")

obj=Child()
obj.ParentClassMethod()
obj.ChildClassMethod()