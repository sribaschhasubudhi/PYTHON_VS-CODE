import ast
l=ast.literal_eval(input("Enter a list od string:-"))
for i in range(len(l)):
    print(l[i],end=" ")