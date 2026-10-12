# write a program to check if a given number is pallindrome or not
n=input("enter the number:-")
ns=str(n)
if ns==ns[::-1]:
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")