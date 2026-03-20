m = int(input("Enter the start : "))
n = int(input("Enter the end : "))
print("Prime numbers : ",end = " ")
for i in range(m,n+1):
    for j in range(2,i):
        if(i%j == 0):
            break
        else:
            print(i,end=", ")