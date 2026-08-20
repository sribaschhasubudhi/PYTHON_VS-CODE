import ast
l=ast.literal_eval(input("Enter the list of numbers:-"))
lc=[]
for i in range(len(l)):
    t=(l[i],l[i]**3)
    lc.append(t)
print("Cube list:-",lc)