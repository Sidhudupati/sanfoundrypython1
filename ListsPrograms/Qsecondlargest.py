n=int(input("Enter no. of elements:"))
a=[]
for i in range(0,n):
    
    
        b=int(input("Enter elements:"))
        a.append(b)
a.sort()        
print("Second largest:",a[n-2])        
