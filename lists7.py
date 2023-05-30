a=int(input("Enter no. ofelements:"))
b=[]
for i in range(0,a):
    elem=int(input("Enter element: "))
    b.append(elem)
avg=sum(b)/a
print("Average of elements in the list",round(avg,2))