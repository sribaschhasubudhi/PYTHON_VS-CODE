M={}
n=int(input("Enter number of students:-"))
for i in range(n):
    roll=int(input("Enter your roll number:-"))
    m1=int(input("enter marks of subject-1:-"))
    m2=int(input("Enter marks of subject-2:-"))
    m3=int(input("Enter marks of subject-3:-"))
    M[roll]=(m1,m2,m3)
print("The roll number- marks list:-",M)