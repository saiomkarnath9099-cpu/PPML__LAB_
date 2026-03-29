num=int(input("Enter a number : "))
per=int(input("Entr perfect number : "))
x=num;sum=0
while(x!=0):
    digi=x%10
    sum+=digi
    x=x//10
if sum==per:
    print(f"{num} is a pefect number.")
else:
    print(f"{num} is not a perfect number.")