num = int(input("Enter a number : "))
i = 1;cnt = 0
while(i<=num):
    if(num%i == 0):
        cnt+=1
    i+=1
if(cnt == 2):
    print(f"{num} is Prime number.")
else:
    print(f"{num} is not a Prime number.")