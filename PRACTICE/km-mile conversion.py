print("If you want to convert miles to kilometre, type '1'")
print("If you want to convert kilometres to miles, press '2'")
ch=int(input("Enter your choice:- "))
# 1 mile = 1.60934 km
if ch==1:
    mil=int(input("Enter mile value in integer:- "))
    if mil!=abs(mil):
        print("Negative input is invalid")
    else:
        kilo=mil*1.60394
        print(mil,"miles= ",kilo, "kilometres")
elif ch==2:
    km=int(input("Enter kilometre value in integers:- "))
    if km!=abs(km):
        print("Negative input is invalid")
    else:
        ml=round(km/1.60394,2)
        print(km,"kilometres= ",ml,"miles")
else:
    print("invalid choice,try again")