import random
def twonos():
    st=int(input("Enter the starting number:-"))
    en=int(input("Enter the stopping number:-"))
    L=[]
    for i in range(3):
        ran=random.randint(st+1,en-1)
        L.append(ran)
    print("The 3 random numbers between",st,"and",en,"are",L)
twonos()