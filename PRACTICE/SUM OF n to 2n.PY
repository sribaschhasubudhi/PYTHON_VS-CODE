n=int(input("Enter an integer:-"))
sum=0
if n==abs(n):
    for i in range(n,(2*n)+1):
        sum=sum+i
    print("Sum of all the integers between",n,"to",2*n,"is",sum)
elif n!=abs(n):
    print("Negative number as input")
    for j in range(2*n,n+1):
        sum=sum+j
    print("Sum of all the integers between",2*n,"to",n,"is",sum)
else:
    print("Integer required as input. Try again")
