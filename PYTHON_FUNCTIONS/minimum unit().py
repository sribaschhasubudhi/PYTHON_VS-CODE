def unit_digit(x,y):
    if int(str(x)[-1])> int(str(y)[-1]):
        print(y,"is the number having the minimum unit digit number")
    elif int(str(x)[-1])< int(str(y)[-1]):
        print(x,"is the number having the minimum unit digit number")
    elif int(str(x)[-1])== int(str(y)[-1]):
        print("Unit digit of both numbers are same")
x=int(input("Enter 1st number:-"))
y=int(input("Enter 2nd number:-"))
unit_digit(x,y)