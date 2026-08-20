askx=input("Do you want to input length (y/n):-")
if askx=="y":
    x=int(input("Enter length of the box:-"))
else:
    x=10
    print("taking default for length; 10")
#
asky=input("Do you want to input breadth (y/n):-")
if asky=="y":
    y=int(input("Enter breadth of the box:-"))
else:
    y=10
    print("taking default for breadth; 10")
#
askz=input("Do you want to input height (y/n):-")
if askz=="y":
    z=int(input("Enter height of the box:-"))
else:
    z=10
    print("taking default for height; 10")
#
def box(l,b,h):
    vol=l*b*h
    print("Volume of the box is",vol)
box(x,y,z)