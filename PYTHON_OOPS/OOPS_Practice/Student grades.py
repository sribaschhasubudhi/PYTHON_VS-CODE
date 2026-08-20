# Write a Python program to create a Student class that stores a student’s name and a list of marks. 
# Add a method average() that calculates and returns the average of all marks.
import ast
class Student:
    def __init__(self):
        self.name=input("Enter name of the student:-")
        self.marks=ast.literal_eval(input("Enter the marks in a list"))

    def average(self):
        avg=sum(self.marks)/len(self.marks)
        print(f"{self.name} scored an average of {avg} in each subject")

stud=Student()
stud.average()