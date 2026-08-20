import ast
l=ast.literal_eval(input("Enter the list of numbers:- "))
lst=list(set(l))
lar=max(lst)
lst.remove(lar)
lar2=max(lst)
print("The 2nd largest number in the list is",lar2)