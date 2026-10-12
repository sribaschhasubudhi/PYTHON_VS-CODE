import ast
l=ast.literal_eval(input("Enter the list of string:-"))
w=input("Enter the word to be replaced:-")
rep=input("Enter the new word:-")
for i in range(len(l)):           #i is now the index number
    if l[i]==w:
        l[i]=rep
print("The replaced list:-",l)