# Write a Python program to find the second lowest total marks of any student(s) from the given names and marks of each student using lists and lambda. 
# Input the number of students, the names and marks of each student.

student_count=int(input("Enter the number of students:-"))
report=[]
for i in range(student_count):
    name=input("Enter the name of student:-")
    marks=int(input("Enter the marks obtained by him/her:-"))
    report.append([name,marks])
sorted_report=sorted(report,key=lambda x:x[1])
print(sorted_report)

# Normal Method:-
'''mark_list=[]
for name, marks in sorted_report:
    mark_list.append(marks)
mark_set=sorted(set(mark_list))'''

# List Comprehension Method:-
mark_set=sorted(set(marks for name,marks in sorted_report))
second_lowest_mark=mark_set[1]

# Normal Method:-
'''sec_low_names=[]
for names, marks in sorted_report:
    if marks==mark_set[1]:
        sec_low_names.append(names)
print(f"Names of the student having the second lowest marks: {sec_low_names}")'''

# Lambda Function Method:-
sec_low_report=list(filter(lambda x:x[1]==second_lowest_mark,sorted_report))
sec_low_names=[name for name,marks in sec_low_report]              # List Comprehension Method
print(f"Names of the student having the second lowest marks: {sec_low_names}")