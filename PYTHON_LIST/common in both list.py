import ast
la=ast.literal_eval(input("Enter 1st list:- "))
lb=ast.literal_eval(input("Enter 2nd list:- "))
res=list(set(la)&set(lb))
print("common number list:-",res)