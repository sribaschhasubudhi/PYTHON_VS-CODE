def replicate(s,n):
    print("The Replicated Value:",s*n)
s=input("Enter the string:-")
n=int(input("Enter the number of times to be replicated:-"))
replicate(s,n)

'''In place of "print("Replicated value:-",s*n)", if I had
     wrote "return s*n", it would have printed nothing as 
     output because the fuction calling statement doesn't 
     hold the return output.''' 