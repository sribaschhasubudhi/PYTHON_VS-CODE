s=input("enter the string:- ")
for i in s:
    if i==i.lower():
        print(i.upper(),end="")
    elif i==i.upper():
        print(i.lower(),end="")
    else:
        print(i,end="")