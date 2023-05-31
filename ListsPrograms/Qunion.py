n1=int(input("Enter no. of elements:"))
a=[]
for i in range (0,n1):
    b=int(input("Enter element:"))
    a.append(b)
n2=int(input("Enter no. of elements:"))
b=[]
for i in range (0,n2):
    c=int(input("Enter element:"))
    b.append(c)
union=list(set().union(a,b))
print(union)    
        