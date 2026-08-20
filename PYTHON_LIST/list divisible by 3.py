import ast
l=ast.literal_eval(input("Enter the list of numbers:- "))
for x in l:
    if x%3==0:
        print(x,end=",")
