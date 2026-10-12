#write a program that repeatedly asks user to input numbers until "done" is typed. print sum of the numbers.
num=input("enter number:-")
m=0
sum=0
while num!="done":
    n=int(num)
    m=m+n
    sum=sum+m
    num=input("enter number or type 'done' to quit:-")
print("The sum is:-",sum)