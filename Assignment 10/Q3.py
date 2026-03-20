class Father:
    def Skill1(self):
        print("Skill1")

class Mother:
    def Skill2(self):
        print("Skill2")

class Child(Father,Mother):
    def Skill3(self):
        print("Skill3")

obj = Child()
obj.Skill1()
obj.Skill2()
obj.Skill3()