list1 = ["Apple","Banana","Kiwi","Avocado","Mango"]
print("List from index to first index : ",list1[::-1])
reverse_list = []
for i in list1:
    reverse_list.append(i[::-1])
print("Reversed list : ",reverse_list)
for i in list1:
    print(f"Length of {i} : ",len(i))