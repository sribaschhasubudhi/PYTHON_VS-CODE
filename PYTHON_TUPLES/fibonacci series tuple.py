n=int(input("Enter the terms:-"))
l=[0,1]
for i in range(0,n-2):
    l.append(l[-1]+l[-2])
fibo=tuple(l)
print("Fibonacci tuple series:-",fibo)