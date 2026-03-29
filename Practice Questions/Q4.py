string=input("Enter a string : ")
reverse=''.join(reversed(string))
print("Reversed string is : ",reverse)
cntv,cntc=0,0
for i in string:
    if i in "aeiouAEIOU":
        cntv+=1
    else:
        cntc+=1
print(f"Vowels : {cntv}\nConsonant : {cntc}")