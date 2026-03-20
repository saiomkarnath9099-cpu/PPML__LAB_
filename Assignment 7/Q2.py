m = int(input("Enter the start : "))
n = int(input("Enter the end : "))
l = [x for x in range(m,n+1)]
print("Sum : ",sum(l))
print("The average : ",sum(l)/len(l))
print("Largest element : ",max(l))
print("Smallest : ",min(l))
l2 = [x for x in l if x%3 != 0]
print("Element not divisible by 3 : ",l2) 