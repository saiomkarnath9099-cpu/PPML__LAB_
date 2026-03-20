inp = input("Enter a pragraph : ")
l = inp.split()
print("The paragraph contains ", len(l)," words")
count = 0
for i in l:
    if i == i[::-1]:
        cnt+=1
print("Palindrome : ",count)
print("Reverse order : ")
for i in l:
    print(i[::-1])