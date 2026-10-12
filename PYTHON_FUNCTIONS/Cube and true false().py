# Cube of a number:-
def cube():
    ask=input("do you want to enter the number? (y/n):-")
    if ask=="y":
        x=int(input("Enter the number:-"))
    else :
        print("Taking default value=2")
        x=2
    c3=x**3
    print("Cube of",x,"is",c3)
cube()

# True or False:-
def TF(s):
    s="satun"
    if s==a:
        print("True")
    else:
        print("False")
a=input("Enter the random name:-")
TF(a)