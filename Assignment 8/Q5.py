def check(a):
    for i in range(2,a):
        if a%i == 0:
            return "not"
    return ""
a = int(input("Enter a number : "))
print(f"{a} is {check(a)} a prime number")