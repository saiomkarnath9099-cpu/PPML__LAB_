a=int(input("Enter a : "))
b=int(input("Enter b : "))
print(f"Before swapping a : {a} and b : {b}")
a=a^b
b=a^b
a=a^b
print(f"After swapping a : {a} and b : {b}")