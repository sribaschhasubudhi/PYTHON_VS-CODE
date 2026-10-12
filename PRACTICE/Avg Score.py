name = input("enter your name:-")
marks= int(input("enter your average marks scored:-"))
if marks > 100:
    print("invalid marks entered")
elif marks >= 85:
    print("you are eligible for science")
elif marks >= 75:
    print("you are eligible for commerce")
elif marks >= 65:
    print("you are eligible for humanities")
else:
    print("you are not eligible for any stream")
print("Thank you for using this program")