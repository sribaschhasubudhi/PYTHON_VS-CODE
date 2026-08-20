import ast
l=ast.literal_eval(input("ENTER THE LIST OF NUMBERS:- "))
for i in range(len(l)):
    if l[i]%2==0:
        l[i]=l[i]+5

    elif l[i]%2!=0:
        l[i]=l[i]-2

print(l)
