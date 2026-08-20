def comparelen(a,b):
    if len(a)==len(b):
        print("True;",a,"and",b,"are of same length")
    else:
        print("False;",a,"and",b,"don't have same number of letters")
x=input("Enter 1st string:-")
y=input("Enter 2nd string:-")
comparelen(x,y)