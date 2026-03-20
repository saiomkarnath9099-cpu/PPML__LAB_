class GrandParents:
    def Property(self):
        print("I have the properties")

class Parents(GrandParents):
    def Business(self):
        print("I am a businessman")

class Child(Parents):
    def education(self):
        print("I am a student")

obj=Child()
obj.Property()
obj.Business()
obj.education()
