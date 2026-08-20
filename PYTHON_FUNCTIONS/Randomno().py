import random
def random_num(n):
    st=10**(n-1)
    en=(10**n)-1
    ran=random.randint(st,en)
    print("The random number:-",ran)
n=int(input("Enter the no the digits:-"))
random_num(n)