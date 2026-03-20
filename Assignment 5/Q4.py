list1 = []
n = int(input("Enter the no of elements : "))
for i  in range(n):
    a = int(input("Enter a number : "))
    list1.append(a)
list2 = list(set(list1))
print("No duplicate list : ",list2)
list3 = sorted(list2)
print("Sorted list : ",list3)