a=input("Enter a string:")
char=input("Enter character:")
if char in a:
  print(a.count(char))
  print("Character is present")
else:
  print("character not available")