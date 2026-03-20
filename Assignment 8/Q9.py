def SI(p,r,t):
    return(p*r*t)/100
p = float(input("Enter principal amount : "))
r = float(input("Enter rate of intrest : "))
t = float(input("Enter time period : "))
print("Simple Intrest : ",SI(p,r,t))