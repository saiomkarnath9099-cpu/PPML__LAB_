n = int(input("Enter a number : "))
a = 0
b = 1,cnt = 0
while cnt<n:
    print(a,end=" ")
    a,b = b,a+b
    cnt += 1