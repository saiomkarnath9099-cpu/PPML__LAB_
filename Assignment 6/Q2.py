d={}
n = int(input("Enter number of keyvalue pairs : "))
for i in range(n):
    k = input("Enter key : ")
    v = input("Enter value : ")
    d[k] = v
rev={}
for k,v in d.items():
    rev[v] = k
print("\nOriginal dictonary : ")
print(d)
print("\nReversed dictonary : ")
print(rev)