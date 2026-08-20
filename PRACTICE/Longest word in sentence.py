sen="Brazil has the highest sugarcane production in the world."
l=sen.split()
n=0
long=""
for i in l:
    new=i.strip(".")
    if len(new)>n:
        n=len(new)
        long=new
print("Longest word in the sentence is",long)