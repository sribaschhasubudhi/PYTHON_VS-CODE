'''VERY IMPORTANT'''
# Write a Python program that creates a Vector class representing a 2D vector.
# implements the __add__ dunder method so that two Vector objects can be added using the + operator.

class Vector:
    # Constructor Method
    def __init__(self,x,y):
        self.x=x
        self.y=y

    # Additiion Method
    def __add__(self, other):
        return Vector(self.x + other.x,self.y + other.x)

    # Developer's Representation
    def __repr__(self):
        return f"Vector({self.x},{self.y})"

v1=Vector(2,4)
v2=Vector(3,5)

result=v1+v2
print(result)