list = []
a = 0;b = 1;sum = 0
for i in range(20):
    if a > 1000:
        break
    else:
        list.append(a)
        a,b = b,a+b
print(list)
for j in list:
   if j%2 == 0:
       sum+=j
print("Sum is : ",sum)