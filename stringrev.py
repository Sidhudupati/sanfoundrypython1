def rev(str):
    if len(str) == 0:
        return str
    else:
        return rev(str[1:])+str[0]
a = str(input("Enter a string:"))
print(rev(a))