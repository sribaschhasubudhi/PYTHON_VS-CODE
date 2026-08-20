def AP4():
    a=int(input("Enter the first number:-"))
    d=int(input("Enter step value:-"))
    print("The first four digits of the AP are:-")
    for i in range(1,5):
        t=a+((i-1)*d)
        print(t)
AP4()