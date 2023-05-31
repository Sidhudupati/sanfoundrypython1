a=[]
n=int(input("Enter no. of elements:"))
for i in range(0,n):
    b=int(input("Enter elements:"))
    a.append(b)
a.sort()
even=[]
odd=[]
for i in a:
    if(i%2==0):
        even.append(i)
        even.sort()
    else:
        odd.append(i)
        odd.sort()

print("Even:",even)

print("Odd:",odd) 

