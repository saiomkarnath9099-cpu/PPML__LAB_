a = int(input("Enter side : "))
b = int(input("Enter side : "))
c = int(input("Enter side : "))
sum = a+b+c
s = sum/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area is  : ",area)
print("Perimeter is : ",sum)