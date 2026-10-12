import ast
l=ast.literal_eval(input("Enter the 1st list:-"))
print("WARNING: Both the list must be of same length")
m=ast.literal_eval(input("Enter the 2nd list:-"))
n=[]
for i in range(len(l)):
    n.append(l[i]+m[i])
print("The new list is:-",n)