a=[]
n=int(input("Enter no. of elements:"))
for i in range(0,n):
    b=int(input("Enter elements:"))
    a.append(b)
a.sort()
sum=0
for i in a:
    sum=sum+i
k=sum/n 
print("Average is:",k)   
        