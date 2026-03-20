i = input("Enter sentence : ")
list1 = i.split()
print("\nElements of list1 : ")
for i,w in enumerate(list1):
    print(i,w)
list2 = list(range(1,len(list1)+1))
list3 = list(zip(list1,list2))
print("\nCombined list3 using zip : ")
print(list3)