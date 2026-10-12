import ast
l=ast.literal_eval(input("Enter the list of numbers:-"))
even=[]
ce=0
odd=[]
co=0
for i in l:
    if i%2==0:
        even.append(i)
        ce+=1
    elif i%2!=0:
        odd.append(i)
        co+=1
print("The list contained",ce,"even numbers:-",even)
print("The list contained",co,"odd numbers:-",odd)