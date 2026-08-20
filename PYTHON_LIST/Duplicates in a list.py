import ast
l=ast.literal_eval(input("Enter the list of numbers:-"))
m=set()
new=[]
for i in l:
    if i in m:
        new.append(i)
    else:
        m.add(i)
new=list(set(new))
print(len(new),"duplicate numbers")
print("list of duplicate numbers:-",new)