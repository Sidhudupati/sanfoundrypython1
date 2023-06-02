def check_occurence():
    for target in my_list:
        count=my_list.count(target)   
    if count>1:
        print("False")
    else:
        print("True")    
my_list=[1,4,2,1,2,5,9,8]
check_occurence()