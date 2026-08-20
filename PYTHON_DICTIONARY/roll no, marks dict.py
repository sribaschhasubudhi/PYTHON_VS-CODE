d={}
n=int(input("Enter the number of students:-"))
for i in range(n):
    roll=int(input("Enter your roll number:-"))
    marks=int(input("enter marks:-"))
    d[roll]=marks
print("The dictionary is:-",d)