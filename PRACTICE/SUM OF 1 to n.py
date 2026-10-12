'''write a program to print all numbers from 1 to n'''
n= int(input("enter last number of range:-"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print("number of times iterated :-",i) 
print("sum is :-",sum)
