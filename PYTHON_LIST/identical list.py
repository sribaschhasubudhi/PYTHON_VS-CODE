import ast
la=ast.literal_eval(input("Enter 1st list:- "))
lb=ast.literal_eval(input("Enter 2nd list:- "))
if la==lb:
    print("Both are identical lists")
else:
    print("Both are not identical lists")