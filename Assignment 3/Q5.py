mark1 = float(input("Enter marks : "))
mark2 = float(input("Enter marks : "))
mark3 = float(input("Enter marks : "))
mark4 = float(input("Enter marks : "))
mark5 = float(input("Enter marks : "))
totalMark = mark1+mark2+mark3+mark4+mark5
per = (totalMark/250)*100
if(per >= 90 and per<=100):
    print("Grade : O")
elif(per >= 80 and per<=90):
    print("Grade : E")
elif(per >= 70 and per<=80):
    print("Grade : A")
elif(per >= 60 and per<=70):
    print("Grade : B")
elif(per >= 50 and per<=60):
    print("Grade : C")
else:
    print("Grade : F")