import random
a=[]
n=int(input("Enter no. of elements:"))
for i in range(0,n):
    b=random.randint(1,20)
    a.append(b)
a.sort()   
print(a) 