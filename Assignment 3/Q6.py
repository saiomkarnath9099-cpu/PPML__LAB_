ch = input("Enter a character : ")
for i in "AEIOUaeiou":
    if i == ch:
        print(f"{i}is Vowel")
        break
else:
    print(f"{ch} is Consonant")