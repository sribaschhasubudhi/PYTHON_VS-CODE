sen=input("Enter your sentence:-")
sen2=sen.strip(".")
l=sen.split()
w=len(l)
print("The line has",w,"words")
c=0
for i in sen:
    if i in {".",","," "}:
        c+=1
perc=(w/(w+c))*100
print("the line has",c,"characters")
print("Percentage of characters that are alpha numeric:-",perc,"%")