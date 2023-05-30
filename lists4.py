
def square_of_numbers():
  a=[]
  for i in range(1,31):
    a.append(i**2)
  print("List of squares of numbers except first 5 elements ")  
  print(a[5:])  
 
square_of_numbers()  