string=input("Enter a string : ")
if string == string[::-1]:
    print(f"{string} is Palindrom.")
else:
    print("Reversed string is : ",string[::-1])
    print(f"{string} is not a palindrome.")