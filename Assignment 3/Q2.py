import math
a = float(input("Enter a : " ))
b = float(input("Enter b : " ))
c = float(input("Enter c : " ))
d = (b*b)-(4*a*c)
if(d>0):
    r1 = (-b+ math.sqrt(d))/(2*a)
    r2 = (-b- math.sqrt(d))/(2*a)
    print(f"Real roots are {r1} and {r2}")
elif d == 0:
    r = -b / (b*a)
    print(f"Real roots are {r}")
else:
    print("No real root")