a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
x = a,y = b
while y !=0:
    x,y = y,x%y
m,n = x,c
while n!= 0:
    m,n = n,m%n
print("GCD is : ",m)