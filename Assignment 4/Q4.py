n = int(input("Enter an integer : "))
sum = 0
while n >0:
    digit = n%10
    sum+=digit
    num//=10
print("Sum of digit is : ",sum)