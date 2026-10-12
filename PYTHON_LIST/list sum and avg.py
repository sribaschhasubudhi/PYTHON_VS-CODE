import ast
lst=ast.literal_eval(input("Enter the list of numbers:- "))
sum=0
n=0
for i in lst:       #for i in range(len(lst)):
    sum=sum+i       #sum=sum+lst[i] 
    n=n+1
avg=sum/n
print(n,"numbers are present in the list.")
print("The sum of the numbers present in the list is ",sum)
print("The average of the ",n,"numbers present in the list is ",avg)