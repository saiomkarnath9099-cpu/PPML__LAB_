num = int(input("Enter a number : "))
num1 = num
newNum = 0
while(num !=0):
    digit = num%10
    newNum = (newNum*10)+digit
    num= num//10
print(f"Reversed number is : {newNum}")
if(num1 == newNum):
    print(f"{num1} is a palindrome number")
else:
    print(f"{num1} is not a palindrome number")