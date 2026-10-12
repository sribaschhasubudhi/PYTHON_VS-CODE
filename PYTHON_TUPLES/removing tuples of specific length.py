import ast
l=ast.literal_eval(input("Enter a list of tuples:-"))
k=int(input("Enter the length of tuple to be deleted:-"))
new=[]
for i in range(len(l)):
    if len(l[i])!=k:
        new.append(l[i])
print("The new list:-",new)