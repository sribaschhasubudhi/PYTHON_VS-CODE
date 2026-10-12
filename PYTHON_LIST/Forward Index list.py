import ast
l=ast.literal_eval(input("Enter the list:-"))
n=len(l)
new=l[-1:]+l[:-1]
print("Changed list:-",new)
'''VERY IMPORTANT PROGRAM'''