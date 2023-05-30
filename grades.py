s1=int(input("Enter marks:"))
s2=int(input("Enter marks:"))
s3=int(input("Enter marks:"))
avg=(s1+s2+s3)/3
if(int(avg)>=90):
    print("Grade: A")
elif(int(avg)>=80 and int(avg)<90):
    print("Grade: B")
elif(int(avg)>=70 and int(avg)<80):
    print("Grade: C")
elif(int(avg)>=60 and int(avg)<70):
    print("Grade: D")
else:
    print("Grade: F")