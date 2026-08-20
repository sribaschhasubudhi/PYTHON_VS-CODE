import ast
def LShift(Arr,n):
    new=Arr[n:]+Arr[:n]
    print(new)
Arr=ast.literal_eval(input("Enter the list of numbers:-"))
n=int(input("Enter the shift number:-"))
LShift(Arr,n)