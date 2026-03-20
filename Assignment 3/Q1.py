string = input("Enter a string : ")
reverse = string[::-1]
if(string == reverse):
    print(f"{string} is palindrome string.")
else:
    print(f"{string} is not a palindrome string.")