import ast
l=ast.literal_eval(input("Enter the list of integers:- "))
l=list(set(l))
print("list of unique values from the original list: ",l)