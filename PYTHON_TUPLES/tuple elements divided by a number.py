import ast
l=ast.literal_eval(input('Enter a list of tuples:-'))
n=int(input("Enter the number:-"))
new=[]
for i in range(len(l)):
    for j in l[i]:
        if j%n==0:
            new.append(l[i])
            break
print("the divisible tuple:-",new)