'''print('* ' * 5)
for i in range(3):
    print('*   *')
print('* ' * 5)

    
Not working as expected.

'''
print("*")
c=0
for i in range(1,6):
    if(i%2==0):
        c+=1
    else:
        print("*"+" "*(i)+"*")
print("* * * * *")    
'''    
*
* *
*   *
*     *
* * * * *
'''