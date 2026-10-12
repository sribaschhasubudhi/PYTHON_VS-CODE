#calculate sum of the series:- 1+(1+2)+(1+2+3)+(1+2+3+4)+ ...... +(1+2+3+4+....n)

n=int(input("Enter the number:-"))
sum=0
s=0
for i in range(1,n+1):
    sum=sum+i
    s=s+sum
print(sum)
print(s)