# Write a Python program that defines an Employee base class, 
# then creates FullTimeEmployee and PartTimeEmployee subclasses, 
# each implementing different pay calculation logic.

class Employee:
    def __init__(self):
        self.salary=10000

    def payday(self):
        print(f"You are a {self.etype} Employee. So, your salary is ₹{self.salary}")

class FulltimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.etype="Full time"

class ParttimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.salary+=self.salary*1.5
        self.etype="Part time"

emp=Employee()
person1=FulltimeEmployee()
person1.payday()
person2=ParttimeEmployee()
person2.payday()