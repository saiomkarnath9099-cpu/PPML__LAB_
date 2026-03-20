class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return self.x + other.x,self.y+other.y

p1=Point(1,2)
p2=Point(3,4)
print(p1+p2)

#Further are only for practice n0ot to be writtten in record
class Sub:
    def __init__(self,x):
        self.x=x
    def __sub__(self, other):
        return self.x-other.x
    
s1=Sub(10)
s2=Sub(5)
print(s1-s2)