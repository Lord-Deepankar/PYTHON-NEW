pas = str(input("enter your pass..."))
check = ""
list1 = [ "0","1","2","3","4","5","6","7","8","9"]
for i in list1:
    if i == pas[0]:
        check = check + i
        print(check)                 #checcking first digit of pass
    elif i == pas[1]:
        check = check + i
        print(check)
    elif i == pas[2]:
        check = check + i
        print(check)
    elif i  == pas[3]:
        check = check + i
        print(check) 
if check == pas:
    print("this is your pasword...",check)