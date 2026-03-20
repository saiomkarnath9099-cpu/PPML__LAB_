def vowelcnt(s):
    count = 0
    for i in s:
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            count+=1
    return count
n = input("Enter string : ")
print(f"{n} contains {vowelcnt(n)} vowels" )