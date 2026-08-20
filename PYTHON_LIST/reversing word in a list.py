#VERY VERY IMPORTANT QUESTION
import ast
l=ast.literal_eval(input("Enter a list of strings:-"))
res=[]
for i in l:
    res.append(i[::-1])
print(res)