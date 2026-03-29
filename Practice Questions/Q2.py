num=int(input("Enter a number : "))
x=num;digit=0;digi=0
while(x!= 0):
    digi=x%10
    digit=(digit*10)+digi
    x=x//10
if num==digit:
    print(f"{num} is Palindrome number.")
else:
    print(f"Reversed number is : {digit}")
    print(f"{num} is not a Palindrome number.")
