no=int(input("Enter the number of students:-"))
l=[]
for i in range(0,no):
    roll=int(input("Enter roll number of student:-"))
    name=input("Enter name:-")
    marks=int(input("Enter marks:-"))
    t=(roll,name,marks)
    l.append(t)
l=tuple(l)
print(l)